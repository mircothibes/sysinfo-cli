import subprocess
import sys


def test_text_mode_runs():
    out = subprocess.check_output([sys.executable, "-m", "sysinfo.cli"])
    s = out.decode().lower()
    assert "cpu:" in s
    assert "ram:" in s
    assert "disk:" in s
    assert "net:" in s
    assert "uptime:" in s

