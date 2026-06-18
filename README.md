# ⚡ SysPulse

Real-time system monitoring tool that streams live CPU, RAM, disk, and network
metrics to your browser via WebSockets.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.137-green?logo=fastapi)
![WebSockets](https://img.shields.io/badge/WebSockets-live-orange)
![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)

---

## What It Does

- Streams live system metrics every second via WebSocket
- Displays CPU, RAM, disk, and network usage in a clean dashboard
- Color-coded progress bars — green → yellow → red as usage increases
- Handles multiple concurrent clients independently
- Runs entirely on localhost — no cloud, no account, no setup

---

## Tech Stack

| Layer      | Technology        |
|------------|-------------------|
| Backend    | FastAPI, Python   |
| Real-time  | WebSockets        |
| Metrics    | psutil            |
| Frontend   | Vanilla JS, HTML  |
| Container  | Docker            |

---

## Quick Start

### With Docker
```bash
docker run -p 8000:8000 yashg0/syspulse
```
Open `http://localhost:8000`

### Without Docker
```bash
git clone https://github.com/yashg0/syspulse
cd syspulse
uv sync
uv run uvicorn app.main:app --reload
```
Open `http://localhost:8000`

---

## Project Structure
syspulse/

├── app/

│   ├── main.py       # FastAPI app, routes

│   ├── metrics.py    # psutil metric collection

│   └── ws.py         # WebSocket handler

├── static/

│   └── index.html    # dashboard UI

├── tests/

│   └── test_metrics.py

├── Dockerfile

└── README.md

---

## API

| Method    | Endpoint      | Description              |
|-----------|---------------|--------------------------|
| GET       | `/`           | Serve dashboard          |
| WebSocket | `/ws/monitor` | Stream live metrics      |

---

## Metrics Payload

```json
{
  "cpu": 23.4,
  "memory": {
    "total": 15.01,
    "used": 4.55,
    "available": 10.46,
    "percent": 30.3
  },
  "disk": {
    "total": 463.17,
    "used": 53.55,
    "available": 409.62,
    "percent": 11.6
  },
  "network": {
    "mb_sent": 45.75,
    "mb_received": 524.11
  }
}
```

---

## Roadmap

- [x] V1 — CPU, RAM, disk, network via WebSocket
- [ ] V2 — Top processes by CPU and memory
- [ ] V3 — Docker/Podman container monitoring
- [ ] V4 — Alert system (CPU > 90% → notify)
- [ ] V5 — Historical snapshots with PostgreSQL

---

## Author

**Yash G** — [github.com/yashg0](https://github.com/yashg0)