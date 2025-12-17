import os

from vom.resources.scripts.repo import Repo
from vom.resources.scripts.file import File
from vom.resources.scripts.string import String
from vom.resources.scripts.errors import ImplementationAlreadyExistsError
from vom.resources.scripts.git import Git


HERE: File = File(__file__)

def impl(args: list[str]) -> None:
    repo: Repo = Repo(File(os.getcwd()))
    command: str = args.pop(0)
    match command:
        case "create":
            if not file.
            file: File = (repo.file / String.repo.implementationDir(implementation=args[0]))
            if file.exists():
                raise ImplementationAlreadyExistsError(String.impl.errorImplementationAlreadyExists(implementation=args[0]))
            file.mkdir()
            (file / "info").mkdir()
            (file / "info" / "owner.txt").write(Git.getUsername())
            (file / "commits").mkdir()
            (file / "track").mkdir()
            print(String.impl.createSuccess(file=file))