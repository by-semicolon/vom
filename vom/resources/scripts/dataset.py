from typing import Any

from vom.resources.scripts.encryption import EncryptionService
from vom.resources.scripts.json import JSONFile, EncryptedJSONFile
from vom.resources.scripts.user import User


class JSONDataset:
    def __init__(self, file: JSONFile, data: Any = None) -> None:
        self.file: JSONFile = file
        self.data: Any = data or {}
    def write(self) -> None:
        self.file.write(self.data)
    def read(self) -> str:
        self.data = self.file.read()

class EncryptedJSONDataset(JSONDataset):
    def __init__(self, es: EncryptionService, file: JSONFile, data: Any = None) -> None:
        super().__init__(file, data)
        self.es: EncryptionService = es
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