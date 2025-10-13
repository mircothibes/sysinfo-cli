import json
import subprocess
import sys


def test_runs_json():
    out = subprocess.check_output([sys.executable, "-m", "sysinfo.cli", "--json"])
    data = json.loads(out.decode())

    assert isinstance(data, dict)
    for k in ["cpu", "ram", "disk", "net", "uptime"]:
        assert k in data
