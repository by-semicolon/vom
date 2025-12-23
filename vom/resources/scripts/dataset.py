from typing import Any

from .encryption import EncryptionService
from .json import JSONFile, EncryptedJSONFile
from .user import User


class JSONDataset:
    def __init__(self, file: JSONFile | None = None, data: Any = None) -> None:
        self.file: JSONFile = file
        self.data: Any = data or {}
    def write(self) -> None:
        self.file.write(self.data)
    def read(self) -> None:
        self.data = self.file.read()

class EncryptedJSONDataset(JSONDataset):
    def __init__(self, file: EncryptedJSONFile) -> None:
        super().__init__(None, file.read())
        self.file: EncryptedJSONFile = file

class ContributorsEJDS(EncryptedJSONDataset):
    def addContributor(self, *users: User) -> None:
        for user in users:
            self.data.append(user.toDict())
            self.write()
    def removeContributor(self, *users: User) -> None:
        for user in users:
            self.data.remove(user.toDict())
            self.write()
    def get(self) -> list[User]:
        return [User.fromDict(d) for d in self.data]