import os

from ..resources.scripts.file import File
from ..resources.scripts.repo import Repo
from ..resources.scripts.errors import AlreadyARepoError
from ..resources.scripts.string import String


def init(args: list[str]) -> None:
    file: File = File(args[0] if len(args) > 0 else os.getcwd())
    if not file.exists():
        raise FileNotFoundError(String.init.errorFileNotFound(file=file))
    if "--force" in args:
        (file / ".vom").delete()
    if (file / ".vom").exists():
        raise AlreadyARepoError(String.init.errorAlreadyARepo(file=file))
    Repo.make(file).setup()
    print(String.init.success(formatted=True, parent=file))