import argparse
import re
import subprocess
from typing import List


def separate_tests(separator_char: str = None) -> List[str]:
    sep = {"F": "Function", "C": "Class", "M": "Module"}

    command = "pytest --collectonly"

    pytest_result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    lines = [x for x in str(pytest_result.stdout).split("\\n")]

    pattern = ".*<{} (.*)>.*".format(sep[separator_char])
    tests_list = [matched.group(1) for x in lines if (matched := re.match(pattern, x))]
    return tests_list


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-s",
        "--separator",
        type=str,
        dest="separator",
        required=False,
        default="F",
        help="Use separates flas for split tests\n F - for Function\nC - For Class\nM - for Module",
    )
    args = argparser.parse_args()

    result = separate_tests(separator_char=args.separator)
    print(" ".join(result))
