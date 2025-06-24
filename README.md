
---

### 9. Log Analyzer

```markdown
# 🔍 Log Analyzer for Threat Patterns

> Analyzes log files for common security threat patterns using regex.

## Description

Parses a log file and searches for suspicious events like failed logins, port scans, or SQL injection attempts. Useful for basic threat detection learning.

## Features

- Detects failed SSH login attempts  
- Flags Nmap port scans  
- Looks for SQL injection patterns

## Requirements

No external dependencies; standard Python only.

## Usage

Prepare a log file named `example.log`, then run:

```bash
python log_analyzer.py
