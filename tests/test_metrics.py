from app.metrics import (
    bytes_to_gb,
    bytes_to_mb,
    get_all_metrics,
    get_cpu_usage,
    get_disk,
    get_memory,
    get_network,
)


def test_bytes_to_gb():
    assert bytes_to_gb(1073741824) == 1.0
    assert bytes_to_gb(0) == 0.0


def test_bytes_to_mb():
    assert bytes_to_mb(1048576) == 1.0
    assert bytes_to_mb(0) == 0.0


def test_cpu_usage():
    cpu = get_cpu_usage()
    assert isinstance(cpu, dict)
    assert "overall" in cpu
    assert "cores" in cpu
    assert "count" in cpu
    assert 0.0 <= cpu["overall"] <= 100.0
    assert isinstance(cpu["cores"], list)
    assert len(cpu["cores"]) > 0


def test_memory():
    mem = get_memory()
    assert "total" in mem
    assert "used" in mem
    assert "available" in mem
    assert "percent" in mem
    assert 0.0 <= mem["percent"] <= 100.0


def test_disk():
    disk = get_disk()
    assert "total" in disk
    assert "used" in disk
    assert "available" in disk
    assert 0.0 <= disk["percent"] <= 100.0


def test_network():
    net = get_network()
    assert "mb_sent" in net
    assert "mb_received" in net
    assert "upload_kb" in net
    assert "download_kb" in net


def test_all_metrics_keys():
    metrics = get_all_metrics()
    assert "cpu" in metrics
    assert "memory" in metrics
    assert "disk" in metrics
    assert "network" in metrics
    assert "system" in metrics
    assert "processes" in metrics


def test_system_info():
    from app.metrics import get_system_info
    info = get_system_info()
    assert "hostname" in info
    assert "os" in info
    assert "uptime" in info
    assert len(info["hostname"]) > 0