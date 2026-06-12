services = ["nginx", "docker", "jenkins", "mysql"]
for service in services:
    if service == "docker":
        print("[SKIP] Docker check skipped\n")
        continue
    print(f"[INFO] Checking {service}")
    print("[OK] {service} is running\n")

# Skip invalid files
files = ["app.log", "data.txt", "error.log", "config.json"]

for file in files:
    if not file.endswith(".log"):
        print(f"[SKIP] Not a log file: {file}")
        continue

    print(f"[PROCESS] Log file: {file}")