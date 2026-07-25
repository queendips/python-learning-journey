import time

print(time.time())
# time.sleep(seconds)
print("Start")

time.sleep(3)

print("End")
# 
# while True:
#     print("Checking website...")
#     time.sleep(10)
#-----------------------

current = time.localtime()

print(current)

#time.strftime(format)
print(time.strftime("%d-%m-%Y"))
print(time.strftime("%A"))
print(time.strftime("%B"))
print(time.strftime("%I:%M:%S %p"))
print(time.ctime())

# time.perf_counter()?

# Returns a high-resolution timer used to measure the execution time of code accurately.
start = time.perf_counter()

for i in range(1000000):
    pass

end = time.perf_counter()

print("Execution Time:", end - start)