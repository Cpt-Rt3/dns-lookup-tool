import socket
from datetime import datetime

# 🔹 Banner
print("="*50)
print("⚡ Port Scanner by RT3 ⚡")
print(f"Scan started at: {datetime.now()}")
print("="*50)

# 🔹 Target host and port range
target = input("Enter the IP address to scan: ")
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # timeout for response

    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    sock.close()

print("\nScan complete.")