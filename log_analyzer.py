# log_analyzer.py
import re

LOG_FILE = "example.log"

with open(LOG_FILE, "r") as file:
    lines = file.readlines()

# Example threat patterns
patterns = {
    "Failed SSH login": r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)",
    "Port scan": r"Nmap scan report for",
    "SQL Injection attempt": r"(SELECT|UNION|DROP TABLE).*--",
}

print("[*] Scanning log file for threat patterns...\n")

for threat, pattern in patterns.items():
    matches = [line for line in lines if re.search(pattern, line, re.IGNORECASE)]
    if matches:
        print(f"[!] {threat}: {len(matches)} matches")
        for match in matches[:5]:
            print("    →", match.strip())
        print()
    else:
        print(f"[✓] {threat}: No matches found.\n")
