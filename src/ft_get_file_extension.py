import os

def get_file_extension(file_name: str) -> str:
    """
        returns bla.txt  txt
        .txt -> ""
        "" -> ""
    """
    return os.path.splitext(file_name)[1][1:]
