# Exponential Backoff
import time
wait_time=1
attempt=0
while attempt<5:
    print("Attempts:",attempt+1,", Wait time is ",wait_time,"sec")
    time.sleep(wait_time)
    wait_time*=2
    attempt+=1
