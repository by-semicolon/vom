from .system import get
from uuid import getnode as getNode


class Git:
    @staticmethod
    def getLocalUsername() -> str:
        return get(".", ["git", "config", "user.name"]).stdout.strip()
    @staticmethod
    def getLocalEmail() -> str:
        return get(".", ["git", "config", "user.email"]).stdout.strip()
    @staticmethod
    def getLocalID() -> str:
        return str(getNode())