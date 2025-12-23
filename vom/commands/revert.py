from ..resources.scripts.commit import Commit
from ..resources.scripts.errors import InvalidNumberError
from ..resources.scripts.repo import Repo


def revert(args: list[str]) -> None:
    repo: Repo = Repo(File())
    user: User | None = repo.getUserIfContributor()
    args = args if len(args) < 1 else [len((user.opened.file / "commits").getChildren())]
    try:
        commit: Commit | None = user.opened.getCommitByOrder(int(args[0]))
        if commit is None:
            raise ValueError
    except ValueError:
        raise InvalidNumberError(String.rvrt.errorInvalidNumber())
    if promptConfirmation(String.rvrt.revertConfirmation(implementation=(user.opened if user else "<unknown>"), order=args[0])):
        for file in File().getChildren():
            if file.getFileName() != ".vom" and not VomIgnore().isIgnored(file):
                file.remove()
        commit.moveDecryptedFilesTo(".", replace=False, log=True)