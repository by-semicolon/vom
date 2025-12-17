from vom.resources.scripts.file import File
from vom.resources.scripts.string import String
from vom.resources.scripts.user import User


class Implementation:
    def __init__(self, file: File) -> None:
        self.file: File = file
        self.name: str = file.getFileName()
        self.owners: list[User] = []
    def addOwner(self, *users: User) -> None:
        for user in users:
            self.owners.append(user)
    def removeOwner(self, *users: User) -> None:
        for user in users:
            self.owners.append(user)