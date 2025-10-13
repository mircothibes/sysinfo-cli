import argparse
import json

def get_sysinfo():
    # All: Fill with stdlib (/proc/*, shutil, os)
    return {"cpu": {}, "ram": {}, "disk": {}, "net": {}, "uptime": {}}

def main():
    p = argparse.ArgumentParser(prog="sysinfo-cli")
    p.add_argument("--json", action="store_true", help="JSON output")
    args = p.parse_args()

    data = get_sysinfo()
    if args.json:
        print(json.dumps(data, ensure_ascii=False))
    else:
        print("CPU: ...\nRAM: ...\nDISK: ...\nNET: ...\nUPTIME: ...")


if __name__ == "__main__":
    main()

