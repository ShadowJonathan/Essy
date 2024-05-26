import os
from pathlib import Path

from typing import Union, Iterator


_DEV_FOLDER = "./_domain/"


def domain_folder(domain: str) -> Path:
    return Path(_DEV_FOLDER) / domain


# TODO replace with below and proper method
# def domain_folder(domain: str) -> Path:
#     raise NotImplementedError  # todo


def real_path(domain: str, file_path: Union[str, Path]) -> Path:
    file_path = Path(file_path)

    if file_path.is_absolute():
        file_path = file_path.relative_to(file_path.root)

    return domain_folder(domain) / file_path


def files_for(domain: str) -> Iterator[str]:
    d_folder = domain_folder(domain).resolve()

    # FIXME: this will maybe do weird stuff for windows
    absolute_root = Path("/")

    for root, dirs, files in os.walk(d_folder):
        for file in files:
            path = Path(root) / file
            yield str(absolute_root / path.relative_to(d_folder))


def delete_file(domain: str, path: str):
    os.remove(real_path(domain, path))
