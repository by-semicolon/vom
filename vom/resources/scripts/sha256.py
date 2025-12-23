import hashlib
import json
from typing import Any


class SHA256Parser:
    def __init__(self, data: dict[str, Any]) -> None:
        self.data: dict[str, Any] = data
    def generateCommitID(self) -> str:
        return hashlib.sha256(
            json.dumps(self.data, sort_keys=True).encode('utf-8')
        ).hexdigest()