from vom.resources.scripts.system import get


class Git:
    @staticmethod
    def getLocalUsername() -> str:
        return get(".", ["git", "config", "user.name"]).stdout.strip()
    @staticmethod
    def getLocalEmail() -> str:
        return get(".", ["git", "config", "user.email"]).stdout.strip()