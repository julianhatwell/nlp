from typing import Dict, List, Union
from pathlib import PosixPath
from platform import python_version


def convert_char_to_int(data: List[str], offset:int=97) -> List[int]:
    """
    Converts each char of a string to an int

    :param data: list of a string
    :param offset: offset to set int(0) e.g. 97 for lower cases

    :return: list of mapped integer
    """
    int_list = []

    for i in data:

        int_list.append(ord(i)-offset)

    return int_list


def counter(values: List[Union[int, float, str]]) -> Dict:
    """
        Docstrings are important! :D
    """
    counter = {}
    for i in values:
        counter[i] = counter.get(i, 0) + 1

    return counter


def load_text(path: PosixPath) -> List[str]:
    """
    """
    with open(path) as input:
        text_file = input.readlines()

    text_file = [text.strip("\n") for text in text_file]

    return text_file


def save_text(path: PosixPath, data: List[str]) -> None:
    """
    """
    with open(path, "w") as output:
        output.write('\n'.join(data))

    return None


def write_fasttext_text(
    path: PosixPath, data: List[str], labels: List[str]
) -> None:
    """
    """
    
    version = python_version().split(".")
    version = float(f"{version[0]}.{version[1]}")
    
    if version >= 3.8:
        path.unlink(missing_ok=True)
    else:
        try:
            path.unlink()
        except:
            pass

    with open(path, "a") as output:

        for x, y in zip(data, labels):

            label = f"__label__{y}"

            output.writelines(" ".join([label, x, "\n"]))

    return None
