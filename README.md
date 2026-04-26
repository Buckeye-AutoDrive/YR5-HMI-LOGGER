

TO use this:
```python
import sys
sys.path.insert(0, "/home/autodrive/HMI/YR5-HMI-LOGGER")
import HMI_LOGGER
hmi = HMI_LOGGER.HMI_LOGGER("PREAMBLE in String")       # PERCEPTION, CONTROLS, etc.
hmi.log("Log msg in String")
```

