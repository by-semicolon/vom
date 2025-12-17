from typing import Any
import json

from vom.resources.scripts.encryption import EncryptionService
from vom.resources.scripts.file import File


class JSONFile(File):
    def read(self) -> Any:
        return json.loads(super().read())
    def write(self, object: Any) -> "JSONFile":
        super().write(json.dumps(object))
        return self
    @staticmethod
    def jsonToPython(string: str) -> Any:
        return json.loads(string)
    @staticmethod
    def pythonToJson(object: Any) -> str:
        return json.dumps(object)

class EncryptedJSONFile(File):
    def __init__(self, es: EncryptionService, path: "str | File") -> None:
        self.es: EncryptionService = es
        self.path: str = path.path if isinstance(path, File) else path
    def read(self) -> Any:
        return json.loads(self.es.decrypt(super().read()))
    def write(self, object: Any) -> "JSONFile":
        super().write(self.es.encrypt(json.dumps(object)))
        return self