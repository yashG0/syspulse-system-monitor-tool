from typing import Any

import psutil


def bytes_to_gb(b: int) -> float:
    return round(b / (1024**3), 2)


def bytes_to_mb(b: int) -> float:
    return round(b / (1024**2), 2)


def get_cpu_usage() -> float:
    return round(psutil.cpu_percent(None) / psutil.cpu_count(), 2)


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


def get_network() -> dict[str, Any]:
    net = psutil.net_io_counters()
    return {
        "mb_sent": bytes_to_mb(net.bytes_sent),
        "mb_received": bytes_to_mb(net.bytes_recv),
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
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return sorted(processes, key=lambda x: x["cpu_percent"], reverse=True)[:limit]


def get_all_metrics() -> dict[str, Any]:
    return {
        "cpu": get_cpu_usage(),
        "memory": get_memory(),
        "disk": get_disk(),
        "network": get_network(),
        "processes": get_top_processes(),
    }
