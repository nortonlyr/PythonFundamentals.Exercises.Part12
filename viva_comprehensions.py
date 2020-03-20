from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start:
    :param stop:
    :param parity:
    :return:
    """
    if parity == Parity.ODD:
        return [i for i in range(start, stop) if i % 2 !=0]
    elif parity == Parity.EVEN:
        return [i for i in range(start, stop) if i % 2 == 0]




def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    dicts = {}
    keys = list(range(start, stop))
    for x in keys:
        dicts[x] = strategy(x)
    return dicts


def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    if val_in.islower():
        x = []
        for i in val_in:
            x.append(i.upper())
        return set(x)
    elif not val_in.isupper():
        x= []
        for i in val_in:
            if i.islower():
                x.append(i.upper())
        return set(x)
    elif val_in.isupper():
       return set()
