class User:
    def __init__(self, username: str, email: str, uuid: str, log: list[str] | None = None) -> None:
        self.username: str = username
        self.email: str = email
        self.uuid: str = uuid
        self.log: list[str] = log or []
    @classmethod
    def fromDict(cls, d: dict) -> "User":
        return cls(
            d["username"],
            d["email"],
            d["uuid"],
            d["log"]
        )
    def toDict(self) -> dict:
        return {
            "username": self.username,
            "email": self.email,
            "uuid": self.uuid,
            "log": self.log
        }
    def __eq__(self, other: "User") -> bool:
        return self.uuid == other.uuid