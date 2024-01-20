from hypothesis.strategies import text
from hypothesis import given, settings
import ft_get_file_extension
import os

test_count = int(os.environ["TEST_COUNT"])

@given(name=text(),
       extension=text(alphabet='abcdefghijklmnopqrstuvwxyz'))
@settings(max_examples=test_count)
def test_get_file_extension(name, extension):
    file_name = name + "." + extension
    extension = ft_get_file_extension.get_file_extension(file_name)
    if extension != "":
        assert file_name != "" and extension != ""
    else:
        assert file_name == "" or extension == ""
