import argparse
import json
import os
import shutil
from typing import Any


def _read_meminfo() -> dict[str, int]:
    out: dict[str, int] = {}
    with open("/proc/meminfo", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                k, v = line.split(":", 1)
                num = "".join(ch for ch in v if ch.isdigit())
                if num:
                    out[k.strip()] = int(num)  # kB
    return out


def _ram_info() -> dict[str, Any]:
    m = _read_meminfo()
    total_kb = m.get("MemTotal", 0)
    avail_kb = m.get("MemAvailable", 0)
    used_kb = max(total_kb - avail_kb, 0)
    percent = (used_kb / total_kb * 100) if total_kb else 0.0
    return {
        "total_kb": total_kb,
        "available_kb": avail_kb,
        "used_kb": used_kb,
        "percent": round(percent, 2),
    }


def _disk_info(path: str = "/") -> dict[str, Any]:
    du = shutil.disk_usage(path)
    percent = (du.used / du.total * 100) if du.total else 0.0
    return {
        "path": path,
        "total_bytes": du.total,
        "used_bytes": du.used,
        "free_bytes": du.free,
        "percent": round(percent, 2),
    }


def _cpu_info() -> dict[str, Any]:
    cores = os.cpu_count() or 0
    try:
        load1, load5, load15 = os.getloadavg()
    except OSError:
        load1 = load5 = load15 = 0.0
    return {"cores": cores, "loadavg": {"1m": load1, "5m": load5, "15m": load15}}


def _uptime_info() -> dict[str, Any]:
    with open("/proc/uptime", encoding="utf-8") as f:
        first = f.read().split()[0]
    seconds = float(first)
    return {"seconds": int(seconds)}


def _net_info() -> dict[str, Any]:
    totals = {"rx_bytes": 0, "tx_bytes": 0}
    per_iface: dict[str, dict[str, int]] = {}
    with open("/proc/net/dev", encoding="utf-8") as f:
        lines = f.readlines()[2:]
    for line in lines:
        if ":" not in line:
            continue
        iface, rest = line.split(":", 1)
        iface = iface.strip()
        cols = rest.split()
        rx = int(cols[0])
        tx = int(cols[8])
        per_iface[iface] = {"rx_bytes": rx, "tx_bytes": tx}
        totals["rx_bytes"] += rx
        totals["tx_bytes"] += tx
    return {"total": totals, "interfaces": per_iface}


def get_sysinfo() -> dict[str, Any]:
    return {
        "cpu": _cpu_info(),
        "ram": _ram_info(),
        "disk": _disk_info("/"),
        "net": _net_info(),
        "uptime": _uptime_info(),
    }


def main():
    p = argparse.ArgumentParser(
        prog="sysinfo-cli",
        description=(
            "Show CPU, RAM, disk, network, and uptime." "Use --json for JSON output.",
        ),
    )

    p.add_argument("--version", action="version", version="sysinfo-cli 0.1.0")

    p.add_argument("--json", action="store_true", help="JSON output")
    args = p.parse_args()

    data = get_sysinfo()
    if args.json:
        print(json.dumps(data, ensure_ascii=False))
    else:
        print(f"CPU: cores={data['cpu']['cores']} load={data['cpu']['loadavg']}")
        print(
            f"RAM: used={data['ram']['used_kb']}kB/"
            f"{data['ram']['total_kb']}kB ({data['ram']['percent']}%)"
        )
        print(
            f"DISK: used={data['disk']['used_bytes']}/"
            f"{data['disk']['total_bytes']} ({data['disk']['percent']}%)"
        )
        print(
            f"NET: total_rx={data['net']['total']['rx_bytes']} "
            f"total_tx={data['net']['total']['tx_bytes']}"
        )
        print(f"UPTIME: {data['uptime']['seconds']}s")


if __name__ == "__main__":
    main()
