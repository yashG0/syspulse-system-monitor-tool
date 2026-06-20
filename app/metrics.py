import platform
import socket
import time
from typing import Any

import psutil


def bytes_to_gb(b: int) -> float:
    return round(b / (1024**3), 2)


def bytes_to_mb(b: int) -> float:
    return round(b / (1024**2), 2)


def get_system_info() -> dict[str, Any]:
    uptime_seconds = int(time.time() - psutil.boot_time())
    hours = uptime_seconds // 3600
    minutes = (uptime_seconds % 3600) // 60

    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.release(),
        "uptime": f"{hours}h {minutes}m",
        "cpu_model": platform.processor() or "Unknown",
    }


def get_cpu_usage() -> dict[str, Any]:
    overall = round(psutil.cpu_percent(interval=None) / psutil.cpu_count(), 2)
    per_core = psutil.cpu_percent(interval=None, percpu=True)
    return {
        "overall": overall,
        "cores": per_core,
        "count": psutil.cpu_count(),
    }


def get_memory() -> dict[str, Any]:
    ram = psutil.virtual_memory()
    return {
        "total": bytes_to_gb(ram.total),
        "used": bytes_to_gb(ram.used),
        "available": bytes_to_gb(ram.available),
        "percent": ram.percent,
    }


def get_disk() -> dict[str, Any]:
    disk = psutil.disk_usage("/")
    return {
        "total": bytes_to_gb(disk.total),
        "used": bytes_to_gb(disk.used),
        "available": bytes_to_gb(disk.free),
        "percent": disk.percent,
    }


_last_net = None
_last_net_time = None


def get_network() -> dict[str, Any]:
    global _last_net, _last_net_time

    current = psutil.net_io_counters()
    now = time.time()

    if _last_net is None:
        _last_net = current
        _last_net_time = now
        return {
            "mb_sent": bytes_to_mb(current.bytes_sent),
            "mb_received": bytes_to_mb(current.bytes_recv),
            "upload_kb": 0.0,
            "download_kb": 0.0,
        }

    elapsed = now - _last_net_time  # type:ignore
    upload_kb = round((current.bytes_sent - _last_net.bytes_sent) / elapsed / 1024, 2)
    download_kb = round((current.bytes_recv - _last_net.bytes_recv) / elapsed / 1024, 2)

    _last_net = current
    _last_net_time = now

    return {
        "mb_sent": bytes_to_mb(current.bytes_sent),
        "mb_received": bytes_to_mb(current.bytes_recv),
        "upload_kb": upload_kb,
        "download_kb": download_kb,
    }


cpu_count = psutil.cpu_count()


def get_top_processes(limit: int = 10) -> list[dict[str, Any]]:
    processes = []
    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            processes.append(
                {
                    "pid": proc.info["pid"],
                    "name": proc.info["name"],
                    "cpu_percent": round(proc.info["cpu_percent"] / cpu_count, 2),
                    "memory_percent": round(proc.info["memory_percent"], 2),
                }
            )
        except psutil.NoSuchProcess, psutil.AccessDenied:
            continue

    return sorted(processes, key=lambda x: x["cpu_percent"], reverse=True)[:limit]


def get_all_metrics() -> dict[str, Any]:
    return {
        "system": get_system_info(),
        "cpu": get_cpu_usage(),
        "memory": get_memory(),
        "disk": get_disk(),
        "network": get_network(),
        "processes": get_top_processes(),
    }
