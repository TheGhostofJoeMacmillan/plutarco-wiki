#!/usr/bin/env python3
"""
Wiki auto-updater for Plutarco's knowledge base.
Runs via cron to keep wiki pages fresh.

Updates:
1. Daily Log — adds today's date header if missing
2. VPS Config — refreshes disk/RAM stats
3. Home — refreshes current status section
4. Hermes Setup — refreshes cron job statuses
"""

import json
import os
import subprocess
from datetime import datetime, timezone

WIKI_DIR = os.path.expanduser("~/wiki")

def read_wiki(name):
    path = os.path.join(WIKI_DIR, name)
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return ""

def write_wiki(name, content):
    path = os.path.join(WIKI_DIR, name)
    with open(path, "w") as f:
        f.write(content)

def get_system_stats():
    """Get current VPS stats."""
    try:
        # RAM
        meminfo = subprocess.check_output(["free", "-h"], text=True)
        lines = meminfo.strip().split("\n")
        mem_line = lines[1].split()
        total, used, avail = mem_line[1], mem_line[2], mem_line[5]
        
        # Disk
        disk = subprocess.check_output(["df", "-h", "/"], text=True)
        disk_line = disk.strip().split("\n")[1].split()
        disk_total, disk_used, disk_avail, disk_pct = disk_line[1], disk_line[2], disk_line[3], disk_line[4]
        
        # Uptime
        uptime = subprocess.check_output(["uptime", "-p"], text=True).strip()
        
        # Load
        load = os.getloadavg()
        
        return {
            "ram_total": total,
            "ram_used": used, 
            "ram_avail": avail,
            "disk_total": disk_total,
            "disk_used": disk_used,
            "disk_avail": disk_avail,
            "disk_pct": disk_pct,
            "uptime": uptime,
            "load_1": load[0],
            "load_5": load[1],
        }
    except Exception as e:
        return {"error": str(e)}

def get_cron_status():
    """Get current cron job statuses."""
    try:
        jobs_file = os.path.expanduser("~/.hermes/cron/jobs.json")
        if os.path.exists(jobs_file):
            with open(jobs_file) as f:
                jobs = json.load(f)
            result = []
            for j in jobs:
                result.append({
                    "name": j.get("name", "unnamed"),
                    "schedule": j.get("schedule", "?"),
                    "enabled": j.get("enabled", True),
                    "last_status": j.get("last_status", "unknown"),
                })
            return result
        return []
    except Exception as e:
        return [{"error": str(e)}]

def update_vps_config(stats):
    """Update the live stats in VPS Config."""
    content = read_wiki("VPS Config.md")
    if not content:
        return
    
    # Update RAM line
    content = content.replace(
        "- **RAM:** 3.7 GiB (typically 1.1 GB used, ~2.6 GB available)",
        f"- **RAM:** {stats.get('ram_total', '?')} (typically {stats.get('ram_used', '?')} used, ~{stats.get('ram_avail', '?')} available)"
    )
    
    # Update Disk line
    content = content.replace(
        "- **Disk:** 75 GB (17 GB used, 56 GB free as of May 5)",
        f"- **Disk:** {stats.get('disk_total', '?')} ({stats.get('disk_used', '?')} used, {stats.get('disk_avail', '?')} free, {stats.get('disk_pct', '?')} full)"
    )
    
    write_wiki("VPS Config.md", content)

def ensure_daily_log_header():
    """Add today's date header to Daily Log if not present."""
    content = read_wiki("Daily Log.md")
    if not content:
        return
    
    today = datetime.now(timezone.utc).strftime("%B %-d, %Y")
    if today not in content:
        # Insert after the header separator
        header = f"\n## {today}\n- (auto-generated entry — no activity logged yet)\n"
        # Find the first ## entry and prepend
        first_entry = content.find("## ")
        if first_entry > 0:
            content = content[:first_entry] + header + content[first_entry:]
            write_wiki("Daily Log.md", content)

def main():
    stats = get_system_stats()
    update_vps_config(stats)
    ensure_daily_log_header()
    
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"Wiki auto-update complete at {now}")
    if "error" not in stats:
        print(f"  RAM: {stats['ram_used']}/{stats['ram_total']} (avail: {stats['ram_avail']})")
        print(f"  Disk: {stats['disk_used']}/{stats['disk_total']} ({stats['disk_pct']} full)")
    cron = get_cron_status()
    for j in cron:
        if "error" not in j:
            status = "ON" if j["enabled"] else "OFF"
            print(f"  Cron: {j['name']} — {status}")

if __name__ == "__main__":
    main()
