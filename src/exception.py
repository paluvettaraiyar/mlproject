import sys 
from  src.logger import logging
def exception_details(error,error_message:sys):

    _,_,err_info = error_message.exc_info()
    file_name = err_info.tb_frame.f_code.co_filename
    err_message = "Exception raised in the line [{0}] error message [{1}] in the file[{2}]".format(err_info.tb_lineno,str(error),file_name)
    logging.info(err_message)
    return err_message


class CustomException(Exception):

    def __init__(self,error,error_message:sys):
        super().__init__(error)
        self.error_message = exception_details(error,error_message=error_message)

    def __str__(self) -> str:
        return self.error_message


