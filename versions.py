from itertools import zip_longest
from typing import List


def num_list(version: str) -> List[int]:
    return [int(x) for x in version.split(".")]


def version_compare(version1: str, version2: str) -> int:
    versions = zip_longest(num_list(version1), num_list(version2), fillvalue=0)
    for v1, v2 in versions:
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1

    return 0


print(version_compare("2.1", "2.4.0"))
print("done")
