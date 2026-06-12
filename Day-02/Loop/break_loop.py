# Checking services
services = ["nginx", "docker", "jenkins", "mysql"]
for service in services:
    print(f"[INFO] Checking {service}")
    if service == "jenkins":
        print("[STOP] jenkins service found stopping the loop\n")
        break
    print("[OK] {serivice} is running\n")

# Stop when error log is found
logs = [
    "INFO system started",
    "INFO service running",
    "ERROR database failed",
    "INFO retrying connection"
]
for log in logs:
    print("Reading log: ", log)
    if "ERROR" in log:
        print("[Critical] Error found! Stopping log scan\n")
        break

# Stop deployment if service fails

services = ["nginx", "docker", "jenkins", "mysql"]

for service in services:
    print(f"[DEPLOY] Checking {service}")

    if service == "jenkins":
        print("[FAILED] Jenkins not stable. Stopping deployment!\n")
        break

    print(f"[OK] {service} deployed successfully\n")