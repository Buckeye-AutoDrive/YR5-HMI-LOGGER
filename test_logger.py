import HMI_LOGGER

hmi = HMI_LOGGER.HMI_LOGGER("PERCEPTION")
while True:
    user_input = input("enter message to log (type 'exit' to quit): ")
    if user_input == "exit":
        break
    hmi.log(user_input)