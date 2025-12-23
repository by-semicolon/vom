import os

from ..resources.scripts.ignore import VomIgnore
from ..resources.scripts.dataset import ContributorsEJDS
from ..resources.scripts.commit import Commit
from ..resources.scripts.implementation import Implementation
from ..resources.scripts.json import EncryptedJSONFile, JSONFile
from ..resources.scripts.repo import Repo
from ..resources.scripts.file import File
from ..resources.scripts.prompt import promptConfirmation
from ..resources.scripts.string import String
from ..resources.scripts.errors import ImplementationAlreadyExistsError, UnknownCommandError, ImplementationDoesntExistError, UsageError
from ..resources.scripts.git import Git
from ..resources.scripts.user import User


HERE: File = File(__file__)

def impl(args: list[str]) -> None:
    repo: Repo = Repo(File(os.getcwd()))
    user: User | None = repo.getUserIfContributor()
    if len(args) < 1:
        print(String.misc.info(formatted=True, vom=JSONFile(HERE / ".." / ".." / "vom.json")))
        raise UsageError(String.misc.errorNoCommandPassed())
    command: str = args.pop(0)
    match command:
        case "create":
            if len(args) < 1:
                raise UsageError(String.misc.errorNotEnoughArguments())
            if args[0] == "--user":
                args[0] = user.username if user else Git.getLocalUsername()
            file: File = (repo.file / "implementations" / args[0])
            if "--force" in args:
                file.delete()
            if file.exists():
                raise ImplementationAlreadyExistsError(String.impl.errorImplementationAlreadyExists(implementation=args[0]))
            file.mkdir()
            implementation: Implementation = Implementation(repo.parent, file)
            EncryptedJSONFile(repo.getEncryptionService(), repo.file / "implementations" / implementation.name / "contributors.ejson").write({
                Git.getLocalID(): {
                    "permissions": [],
                    "owner": True
                }
            })
            (file / "commits").mkdir()
            Commit.new(repo.getEncryptionService(), implementation, String.impl.createImplementationCommitMessage(), user, True)
            print(String.impl.createSuccess(formatted=True, implementation=implementation))
        case "list":
            user: User | None = repo.getUserIfContributor()
            for implementation in repo.getImplementations():
                if user is not None and user.opened == implementation:
                    print(String.impl.currentImplementationFormat(implementation=implementation))
                else:
                    print(String.impl.implementationFormat(implementation=implementation))
        case "switch":
            if len(args) < 1:
                raise UsageError(String.misc.errorNotEnoughArguments())
            if args[0] == "--user":
                args[0] = user.username if user else Git.getLocalUsername()
            for implementation in repo.getImplementations():
                if implementation.name == args[0]:
                    break
            else:
                raise ImplementationDoesntExistError(String.impl.errorImplementationDoesntExist(implementation=args[0]))
            commit: Commit | None = implementation.getCommits()[-1]
            if promptConfirmation(String.impl.switchImplementationConfirmation(current_implementation=(user.opened if user else "<unknown>"), implementation=implementation)):
                if user is not None:
                    user.opened = implementation
                    contributors: ContributorsEJDS = repo.getContributorsEJDS()
                    for contributor in contributors.get():
                        if contributor == user:
                            contributor["opened"] = implementation.toDict()
                    contributors.write()
                for file in File().getChildren():
                    if file.getFileName() != ".vom" and not VomIgnore().isIgnored(file):
                        file.remove()
                commit.moveDecryptedFilesTo(repo.getEncryptionService(), File(), replace=False)
        case _:
            raise UnknownCommandError(String.misc.errorUnknownCommand(command=command))