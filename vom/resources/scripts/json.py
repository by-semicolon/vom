from typing import Any
import json

from .encryption import EncryptionService
from .file import File


class JSONFile(File):
    def read(self) -> Any:
        return json.loads(super().read())
    def write(self, obj: Any) -> "JSONFile":
        super().write(json.dumps(obj))
        return self
    @staticmethod
    def jsonToPython(string: str) -> Any:
        return json.loads(string)
    @staticmethod
    def pythonToJson(obj: Any) -> str:
        return json.dumps(obj)

class EncryptedJSONFile(File):
    def __init__(self, es: EncryptionService, path: "str | File") -> None:
        super().__init__(path)
        self.es: EncryptionService = es
    def read(self) -> Any:
        return json.loads(self.es.decrypt(super().read()))
    def write(self, obj: Any) -> "EncryptedJSONFile":
        super().writeBytes(self.es.encrypt(json.dumps(obj)))
        return self