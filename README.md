

TO use this:
```python
# insert this part somewhere in your imports
import sys
sys.path.insert(0, "/home/autodrive/HMI/YR5-HMI-LOGGER")
import HMI_LOGGER
hmi = HMI_LOGGER.HMI_LOGGER("PREAMBLE in String")       # PERCEPTION, CONTROLS, etc.

# use this to send whatever
hmi.log("Log msg in String")
```

