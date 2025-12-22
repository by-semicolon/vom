import os

from ..resources.scripts.string import String
from ..resources.scripts.errors import UsageError
from ..resources.scripts.user import User
from ..resources.scripts.file import File
from ..resources.scripts.repo import Repo
from ..resources.scripts.commit import Commit


HERE: File = File(__file__)

def commit(args: list[str]) -> None:
    if len(args) < 1:
        raise UsageError(String.misc.errorNotEnoughArguments())
    repo: Repo = Repo(File(os.getcwd()))
    user: User | None = repo.getUserIfContributor()
    commit_obj: Commit = Commit.new(repo.getEncryptionService(), user.opened, args[0], user, True)