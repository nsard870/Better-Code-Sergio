# Purpose: To test my patience, Python's limits, and your sense of humor.

import random
import time

print("Launching OMG test sequence...")

time.sleep(1)
print("Thinking really hard about life...")

# Randomly decide if this script succeeds or fails
if random.choice([True, False]):
    print("✅ Success! The script did absolutely nothing, perfectly.")
else:
    raise RuntimeError("OMG! Something went wrong, and we have no idea what.")

print("🎉 OMG test complete. You survived.")
