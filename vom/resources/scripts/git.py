from vom.resources.scripts.system import get


class Git:
    @staticmethod
    def getUsername() -> str:
        return get(".", ["git", "config", "user.name"]).stdout.strip()
    @staticmethod
    def getEmail() -> str:
        return get(".", ["git", "config", "user.email"]).stdout.strip()