# password_hacker (educational demo)

WARNING: This repository is intended for educational and testing purposes only. Do not use these scripts against systems, networks, or accounts you do not own or have explicit permission to test.

## Overview

This small repository contains two example scripts used for learning about authentication testing in a controlled, local environment:

- `hack.py` — demonstration script (intended to run against a local test server).
- `server.py` — minimal local server to demonstrate authentication handling.

The code is provided as-is for study and experimentation in isolated labs only.

## Requirements

- Python 3.8 or newer

No external packages are required unless the scripts import them; check the top of each file for additional dependencies.

## Setup

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows (PowerShell/CMD)
```

2. Inspect the scripts and ensure you understand what they do before running them.

## Usage (local, controlled environment)

Start the test server in one terminal:

```bash
python server.py
```

Run the demonstration script in another terminal:

```bash
python hack.py
```

Only run these scripts on your local machine or on systems where you have explicit permission to perform testing.

## Ethical & Legal Notice

These materials are for learning and defensive security research only. Unauthorized access to systems, data, or services is illegal and unethical. Always obtain written permission before testing systems you do not own.