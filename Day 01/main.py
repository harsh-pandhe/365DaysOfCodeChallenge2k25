import time
import random

message = "Hello, World!"
for char in message:
    print(char, end="", flush=True)
    time.sleep(random.uniform(0.05, 0.2))

print("\nWelcome to the most exciting coding journey!")
