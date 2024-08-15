import os

WEB3_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..", "web3")
DEFAULT_EXCEPTIONS = (
    AssertionError,
    ValueError,
    AttributeError,
    TypeError,
)


def test_no_default_exceptions_are_raised_within_web3py():
    for root, dirs, files in os.walk(WEB3_PATH):
        [dirs.remove(dir_) for dir_ in dirs if dir_ in ("scripts", "module_testing")]
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, encoding="utf-8") as f:
                    for idx, line in enumerate(f):
                        for exception in DEFAULT_EXCEPTIONS:
                            exception_name = exception.__name__
                            if f"raise {exception_name}" in line:
                                raise Exception(
                                    f"``{exception_name}`` raised in web3.py. "
                                    f"Replace with ``Web3{exception_name}``:\n"
                                    f"    file_path:{file_path}\n"
                                    f"    line:{idx + 1}"
                                )
