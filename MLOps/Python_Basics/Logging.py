import logging

# Configure the basic logging settings
# logging.basicConfig(level=logging.DEBUG)

def logConfig():
    logging.basicConfig(
        filename = 'app.log',
        filemode = 'a',
        level = logging.DEBUG,
        format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S'
    )
# logConfig()
# log messages
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")
import logging

## logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithmethicApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a} + {b}= {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None

add(10,15)
subtract(15,10)
multiply(10,20)
divide(20,0)
