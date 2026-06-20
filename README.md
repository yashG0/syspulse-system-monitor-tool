# ⚡ SysPulse

Real-time system monitoring dashboard built with FastAPI, WebSockets, and psutil.
Streams live CPU, memory, disk, network, and process metrics directly to your browser — updated every 3 seconds.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?logo=fastapi)
![WebSocket](https://img.shields.io/badge/WebSocket-Live-orange)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)

---

## Features

- Real-time CPU monitoring — overall usage + per-core breakdown
- Memory usage — used, available, percentage
- Disk usage — used, free, percentage
- Network monitoring — live upload/download KB/s + 30s history graph
- Top 10 processes by CPU with color-coded thresholds
- System info — hostname, OS, uptime
- Color-coded alerts — green → yellow → red as usage increases
- Single Docker command — no setup, no account, no cloud

---

## Quick Start

### Docker

```bash
docker run --pid=host --network=host yashg0/syspulse:latest
```

### Podman

```bash
podman run --pid=host --network=host docker.io/yashg0/syspulse:latest
```

Open `http://localhost:8000`

> `--pid=host` gives access to host process list
> `--network=host` gives access to host network stats
> Without these flags, metrics show container internals instead of your machine

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Runtime | Python 3.14 |
| Real-time | WebSockets, asyncio |
| Metrics | psutil |
| Frontend | Vanilla HTML, CSS, JavaScript |
| Charts | HTML5 Canvas |
| Containerization | Docker, Podman |
| Packaging | uv |
| Testing | pytest |

---

## Local Development

```bash
git clone https://github.com/yashg0/syspulse-system-monitor-tool
cd syspulse-system-monitor-tool/syspulse
uv sync
uv run uvicorn app.main:app --reload
```

Open `http://localhost:8000`

---

## API

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Dashboard UI |
| WebSocket | `/ws/monitor` | Live metrics stream |

---

## Metrics Payload

```json
{
  "system": { "hostname": "fedora", "os": "Linux", "uptime": "9h 7m" },
  "cpu": { "overall": 3.43, "cores": [2.0, 5.0], "count": 12 },
  "memory": { "total": 15.01, "used": 4.36, "available": 10.64, "percent": 29.1 },
  "disk": { "total": 463.17, "used": 54.95, "available": 407.12, "percent": 11.9 },
  "network": { "mb_sent": 2.39, "mb_received": 28.67, "upload_kb": 1.66, "download_kb": 0.82 },
  "processes": [{ "pid": 6200, "name": "firefox", "cpu_percent": 0.86, "memory_percent": 4.87 }]
}
```

---

## Project Structure
syspulse/

├── app/

│   ├── main.py        # FastAPI app, routes, lifespan

│   ├── metrics.py     # psutil metric collection

│   └── ws.py          # WebSocket handler

├── static/

│   └── index.html     # dashboard — HTML + CSS + JS

├── tests/

│   └── test_metrics.py

├── Dockerfile

├── pyproject.toml

├── uv.lock

└── README.md

---

## Roadmap

- [x] CPU monitoring — overall + per core
- [x] Memory monitoring
- [x] Disk monitoring
- [x] Network monitoring — live KB/s + history graph
- [x] Process monitoring — top 10 by CPU
- [x] System info — hostname, OS, uptime
- [x] Color-coded thresholds
- [x] Docker / Podman image
- [ ] Historical metrics storage (PostgreSQL)
- [ ] Alert system (CPU > 90% → notify)
- [ ] GPU monitoring
- [ ] Multi-machine monitoring

---

## Docker Hub

```bash
docker pull yashg0/syspulse:latest
```

[hub.docker.com/r/yashg0/syspulse](https://hub.docker.com/r/yashg0/syspulse)

---

## Author

**Yash G** — [github.com/yashg0](https://github.com/yashg0)

MIT License