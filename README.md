# 🖥️ sysinfo-cli

A simple command-line tool written in pure **Python** that displays system information such as **CPU**, **RAM**, **disk**, **network**, and **uptime**.  
It supports both standard text and JSON output.

---

## 🚀 Quick Start (Local)

```bash
# Clone this repository
git clone https://github.com/mircothibes/sysinfo-cli.git
cd sysinfo-cli

# Create and activate the virtual environment
python -m venv .venv && source .venv/bin/activate

# Install dependencies (development tools included)
pip install -e ".[dev]"

# Run the CLI
python -m sysinfo.cli
python -m sysinfo.cli --json
```

Example output:
```bash
CPU: cores=16 load={'1m': 0.18, '5m': 0.11, '15m': 0.03}
RAM: used=640000kB/8036544kB (7.9%)
DISK: used=3458965504/1081101176832 (0.32%)
NET: total_rx=290 total_tx=42
UPTIME: 21000s
```
---

## 🐳 Docker

You can run the same CLI in a lightweight Docker container.
```bash
# Build the image
docker build -t mvtk/sysinfo-cli:0.1.0 .

# Run it (JSON output)
docker run --rm mvtk/sysinfo-cli:0.1.0 --json

# Or plain text output
docker run --rm mvtk/sysinfo-cli:0.1.0
```

Example JSON output:
```bash
{
  "cpu": {"cores": 16, "loadavg": {"1m": 0.18, "5m": 0.11, "15m": 0.03}},
  "ram": {"total_kb": 8036544, "available_kb": 7397756, "used_kb": 638788, "percent": 7.95},
  "disk": {"path": "/", "total_bytes": 1081101176832, "used_bytes": 3458957312, "free_bytes": 1022649864192, "percent": 0.32},
  "net": {"total": {"rx_bytes": 290, "tx_bytes": 42}},
  "uptime": {"seconds": 20201}
}
```

---

## 🧰 Development

I use Neovim as my main development environment with:
- lazy.nvim
- mason.nvim
- nvim-lspconfig -> (Pyright)
- conform.nvim -> for formatting

Useful Commands
```bash
ruff check .
black .
pytest -q
```

---




