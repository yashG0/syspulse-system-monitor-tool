from typing import Any

import psutil


def bytes_to_gb(b: int) -> float:
    return round(b / (1024**3), 2)


def bytes_to_mb(b: int) -> float:
    return round(b / (1024**2), 2)


def get_cpu_usage() -> float:
    return psutil.cpu_percent()


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
        "available": bytes_to_gb(disk.total - disk.used),
        "percent": disk.percent,
    }


def get_network() -> dict[str, Any]:
    net = psutil.net_io_counters()
    return {
        "mb_sent": bytes_to_mb(net.bytes_sent),
        "mb_received": bytes_to_mb(net.bytes_recv),
    }


def get_all_metrics() -> dict[str, Any]:
    return {
        "cpu": get_cpu_usage(),
        "memory": get_memory(),
        "disk": get_disk(),
        "network": get_network(),
    }
