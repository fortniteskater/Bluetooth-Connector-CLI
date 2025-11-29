import asyncio
import sys
from bleak import BleakClient

async def connect_to_device(address):
    print(f"Attempting to connect to {address}...")
    try:
        async with BleakClient(address) as client:
            print(f"Connected: {client.is_connected}")
            # You can add code here to interact with services/characteristics
            await asyncio.sleep(5) # Stay connected for 5 seconds as a test
        print("Disconnected.")
    except Exception as e:
        print(f"Failed to connect: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python connect.py <bluetooth_mac_address>")
    else:
        device_address = sys.argv[1]
        asyncio.run(connect_to_device(device_address))

