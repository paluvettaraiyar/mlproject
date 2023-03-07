import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"messages",LOG_FILE)
os.makedirs(log_path,exist_ok=True)


LOG_PATHS = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_PATHS,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

if __name__ == "__main__":
    logging.info("This application is started")