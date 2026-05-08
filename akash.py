import os

print("=== Termux Network Scanner ===")

# Install nmap if missing
os.system("pkg install nmap -y")

# Get local network devices
network = input("Enter network range (example 192.168.1.0/24): ")

print(f"\nScanning network: {network}\n")

# Ping scan
os.system(f"nmap -sn {network}")

# Optional detailed scan
target = input("\nEnter target IP for detailed scan (or press Enter to skip): ")

if target:
    print(f"\nDetailed scan for {target}\n")
    os.system(f"nmap -A {target}")

print("\nScan Complete!")
