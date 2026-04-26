import sys
sys.path.insert(0, "/home/autodrive/HMI/YR5-HMI-LOGGER")
import HMI_LOGGER
import time

hmi = HMI_LOGGER.HMI_LOGGER("PERCEPTION")
while True:
    print("bruh")
    time.sleep(1)
    hmi.log("Hello World")