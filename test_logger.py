import HMI_LOGGER

logger = HMI_LOGGER.HMI_LOGGER()
while True:
    user_input = input("enter message to log (type 'exit' to quit): ")
    if user_input == "exit":
        break
    logger.log(user_input)