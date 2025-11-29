# Bluetooth-Connector-CLI

A simple Python script to connect to a specific Bluetooth Low Energy (BLE) MAC address via the command line.

## Prerequisites

*   Python 3.7+ installed.
*   Bluetooth enabled on your machine.
*   Permissions might be required (e.g., running with `sudo` on Linux).

## Installation

1.  Clone this repository:
    ```bash
    git clone github.com
    cd Bluetooth-Connector-CLI
    ```

2.  Install the required Python library:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script from your terminal, replacing `AA:BB:CC:DD:EE:FF` with your target Bluetooth address:

```bash
python connect.py AA:BB:CC:DD:EE:FF
