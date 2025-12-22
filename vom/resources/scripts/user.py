class User:
    def __init__(self, username: str, email: str, uuid: str, opened: "Implementation", owner: bool, log: list[str] | None = None) -> None: # type: ignore <- 'Implementation' undefined to avoid circular import.
        self.username: str = username
        self.email: str = email
        self.id: str = uuid
        self.opened: "Implementation" = opened # type: ignore <- 'Implementation' undefined to avoid circular import.
        self.owner: bool = owner
        self.log: list[str] = log or []
    @classmethod
    def fromDict(cls, d: dict) -> "User":
        from .implementation import Implementation
        return cls(
            d["username"],
            d["email"],
            d["id"],
            Implementation.fromDict(d["opened"]) if d["opened"] else None,
            d["owner"],
            d["log"]
        )
    def toDict(self) -> dict:
        return {
            "username": self.username,
            "email": self.email,
            "id": self.id,
            "opened": self.opened.toDict(),
            "owner": self.owner,
            "log": self.log
        }
    def __eq__(self, other: "User") -> bool:
        return self.uuid == other.uuid