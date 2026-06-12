# # Range Loop
for i in range(5):
    print("Hello", i)

services = ["nginx", "docker", "jenkins", "mysql"]

# Services Loop
for service in services:
    print(f"[INFO] Checking status of {service}")

    # simulation of status check  
    status = "running"   #assuming

    print(f"[OK] {service} is {status}\n")

    #File processing simulation
files = ["app.log", "error.log", "access.log"]
for file in files:
        if file.endswith(".log"):
            print("Processing file:" , file)
# Retry mechanism

import time
for attempt in range(1,4):
     print("Trying connection attempt...", attempt)
     time.sleep(1)