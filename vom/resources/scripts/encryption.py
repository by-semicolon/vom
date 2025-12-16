import sys
import os

from vom.resources.scripts.errors import CryptographyNotInstalledError


try:
    from cryptography.fernet import Fernet
except ModuleNotFoundError:
    raise CryptographyNotInstalledError(f"the 'cryptography' library is not installed on your system but can be installed with '{os.path.basename(sys.executable)} -m pip install cryptography'.")

class EncryptionService:
    def __init__() -> None