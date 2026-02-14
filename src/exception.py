import sys
import types


def error_message_detail(error, error_detail: types.TracebackType):
    file_name = error_detail.tb_frame.f_code.co_filename
    return f"Error in {file_name} at line {error_detail.tb_lineno}: {str(error)}"
