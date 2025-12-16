import os

from vom.resources.scripts.file import File
from vom.resources.scripts.repo import Repo
from vom.resources.scripts.errors import AlreadyARepoError
from vom.resources.scripts.string import String
from vom.resources.scripts.encryption import EncryptionService


def init(args: list[str]) -> None:
    file: File = File(args[0] if len(args) > 0 else os.getcwd())
    if not file.exists():
        raise FileNotFoundError(String.init.errorFileNotFound(file=file))
    elif (file / String.repo.name()).exists() and "--force" not in args:
        raise AlreadyARepoError(String.init.errorAlreadyARepo(file=file))
    Repo.make(file).setup()
    print(String.init.success(formatted=True, parent=file))