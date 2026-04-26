

TO use this:
```python
import HMI_LOGGER

##initliaze this somewhere
logger = HMI_LOGGER.HMI_LOGGER()

while True:

    #user input should be like this: "[peception]: a beutiful message"
    user_input = input("enter message ")
    logger.log(user_input)
```

