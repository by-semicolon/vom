from datetime import datetime
from uuid import uuid4 as createUUID

from vom.resources.scripts.sha256 import SHA256Parser

from .ignore import VomIgnore
from .string import String
from .json import EncryptedJSONFile
from .user import User
from .encryption import EncryptionService
from .file import File


class Commit:
    def __init__(self, file: File, commit_id: str, message: str, author: User, datetime_obj: datetime) -> None:
        self.file: File = file
        self.order: int = int(file.getFileName())
        self.id: str = commit_id
        self.message: str = message
        self.author: User = author
        self.datetime: datetime = datetime_obj
    @classmethod
    def fromDict(cls, d: dict) -> "Commit":
        return cls(
            File(d["file"]),
            d["id"],
            d["message"],
            User.fromDict(d["author"]),
            datetime.fromisoformat(d["datetime"])
        )
    def toDict(self) -> dict:
        return {
            "file": str(self.file),
            "id": self.id,
            "message": self.message,
            "author": self.author.toDict(),
            "datetime": self.datetime.isoformat()
        }
    def moveDecryptedFilesTo(self, es: EncryptionService, destination: File, replace: bool = True) -> None:
        for tree_location, file in destination.getTree(exclude=["info.ejson"]):
            new_file: File = (destination / tree_location / file.getFileName().removesuffix(".e"))
            if replace or not new_file.exists():
                new_file.writeBytes(es.decrypt(file.read()))
    @classmethod
    def new(cls, es: EncryptionService, implementation: "Implementation", message: str, author: User, log: bool = False) -> "Commit": # type: ignore <- 'Repo' and 'Implementation' undefined to avoid circular import.
        file: File = (implementation.file / "commits" / (len((implementation.file / "commits").getChildren()) + 1)).mkdir()
        time: datetime = datetime.now()
        commit: Commit = cls(
            file,
            SHA256Parser({
                "order": int(file.getFileName()),
                "datetime": time.isoformat(),
                "author": author.toDict()
            }).generateCommitID(),
            message,
            author,
            time
        )
        EncryptedJSONFile(es, file / "info.ejson").write(commit.toDict())
        wrote: int = 0
        for tree_location, file2 in File().getTree(exclude=[".vom"]):
            if not VomIgnore().isIgnored(file2):
                new_file: File = (file / tree_location / (file2.getFileName() + ".e"))
                new_file.writeBytes(es.encrypt(file2.read()))
                if log:
                    print(String.cmit.successCopy(formatted=True, file=file2))
                wrote += 1
            elif log:
                print(String.cmit.unsuccessCopy(formatted=True, file=file2))
        print(String.cmit.copyFinished(formatted=True, wrote=wrote))
        return commit