import sys
import os

from vom.resources.scripts.errors import CryptographyNotInstalledError
from vom.resources.scripts.file import File
from vom.resources.scripts.string import String


HERE: File = File(__file__)
KEYS_DIRECTORY: File = (HERE / ".." / ".." / ".." / "keys")

try:
    from cryptography.fernet import Fernet
except ModuleNotFoundError:
    raise CryptographyNotInstalledError(String.encr.errorCryptographyNotInstalled(executable=os.path.basename(sys.executable)), )

class EncryptionService:
    def __init__(self, key: bytes) -> None:
        self.key: bytes = key
        self.fernet: Fernet = Fernet(self.key)
    @classmethod
    def fromRepository(cls, repo: "Repo") -> "EncryptionService": # type: ignore <- 'Repo' is not defined to avoid circular imports.
        return cls((repo.file / "UUID.").readBytes())
    @staticmethod
    def newKey() -> bytes:
        key: bytes = Fernet.generate_key()
        return key
    def encrypt(self, string: str) -> str:
        return self.fernet.encrypt(string)
    def decrypt(self, string: str) -> str:
        return self.fernet.decrypt(string)