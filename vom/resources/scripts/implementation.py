from .commit import Commit
from .file import File
from .string import String
from .user import User
from .json import EncryptedJSONFile


class Implementation:
    def __init__(self, repo_parent: File, file: File) -> None: # type: ignore # <- 'Repo' is undefined to avoid circular import
        from .repo import Repo
        self.repo_parent: File = repo_parent
        self.repo: Repo = Repo(self.repo_parent)
        self.file: File = file
        self.name: str = self.file.getFileName()
    @classmethod
    def fromDict(cls, d: dict) -> "Implementation":
        return cls(
            File(d["repo_parent"]),
            File(d["file"])
        )
    def toDict(self) -> dict:
        return {
            "repo_parent": str(self.repo_parent),
            "file": str(self.file)
        }
    def addOwner(self, *users: User) -> None:
        for user in users:
            self.owners.append(user)
    def removeOwner(self, *users: User) -> None:
        for user in users:
            self.owners.append(user)
    def getOwners(self) -> list[User]:
        return [self.repo.getUserIfContributor(contributor_id) for contributor_id, contributor_info in EncryptedJSONFile(self.repo.getEncryptionService(), (self.repo.file / String.repo.implementationContributorsJson(implementation=self.name))).read().items() if contributor_info["owner"]]
    def getCommits(self) -> list[Commit]:
        return [Commit(
            file,
            (info_json := EncryptedJSONFile(
                self.repo.getEncryptionService(),
                file / "info.ejson"
            ).read())["id"],
            info_json["message"],
            info_json["author"],
            info_json["datetime"]
        ) for file in (self.file / "commits").getChildren()]
    def getCommitByOrder(self, order: int) -> Commit | None:

    def __eq__(self, other: "Implementation") -> bool:
        return self.file == other.file
    def __str__(self) -> str:
        return self.name