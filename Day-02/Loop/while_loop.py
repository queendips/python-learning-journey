# Countdown while loop
count = 5
while count > 0:
    print(count)
    count -= 1
print("Done")

#cpu_usage

cpu_usage = 90
while cpu_usage > 80:
    print(f"[Alert] High CPU : {cpu_usage}% ")
    cpu_usage -=10
    print("CPU utilization is under threshold:", cpu_usage)


# Disk space
disk_usage = 95
while disk_usage > 80:
    print(f"[Alert] High Disk Usage : {disk_usage}%")
    disk_usage -= 5
print("[OK] Disk utilization is under threshold: ", disk_usage)