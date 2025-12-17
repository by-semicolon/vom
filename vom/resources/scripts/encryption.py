import sys
import os

from vom.resources.scripts.errors import CryptographyNotInstalledError
from vom.resources.scripts.file import File
from vom.resources.scripts.json import JSONFile


try:
    from cryptography.fernet import Fernet
except ModuleNotFoundError:
    raise CryptographyNotInstalledError(f"the 'cryptography' library is not installed on your system but can be installed with '{os.path.basename(sys.executable)} -m pip install cryptography'.")

class EncryptionService:
    def __init__(self, key: bytes) -> None:
        self.key: bytes = key
        self.fernet: Fernet = Fernet(self.key)
    @staticmethod
    def newKey() -> bytes:
        key: bytes = Fernet.generate_key()
        return key
    def encrypt(self, string: str) -> str:
        return self.fernet.encrypt(string)
    def decrypt(self, string: str) -> str:
        return self.fernet.decrypt(string)