from uuid import uuid4 as createUUID

from .file import File
from .git import Git
from .json import EncryptedJSONFile, JSONFile
from .string import String
from .errors import NotARepoError, NoKeyError
from .system import run
from .implementation import Implementation
from .encryption import EncryptionService
from .dataset import ContributorsEJDS
from .user import User


HERE: File = File(__file__)
KEYS_DIRECTORY: File = (HERE / ".." / ".." / ".." / "keys")
VOM_JSON: File = (HERE / ".." / ".." / ".." / "vom.json")
README: File = (HERE / ".." / ".." / ".." / "README.txt")

class Repo:
    def __init__(self, parent: File):
        self.parent: File = parent
        self.file: File = self.parent / ".vom"
        if not self.file.exists():
            raise NotARepoError(String.repo.errorNotARepo(file=self.parent))
    def validateKey(self) -> None:
        if not (KEYS_DIRECTORY / self.getUUID()).exists():
            raise NoKeyError("it seems don't have a key to this repository! ask an owner for one before running this command.")
    def getImplementations(self) -> list[Implementation]:
        return [Implementation(self.parent, file) for file in (self.file / "implementations").getChildren()]
    def getUUID(self) -> str:
        return (self.file / "repo" / "uuid.txt").read()
    def getEncryptionService(self) -> EncryptionService:
        return EncryptionService((KEYS_DIRECTORY / (self.getUUID() + ".vom")).read())
    def getContributorsEJDS(self) -> ContributorsEJDS:
        return ContributorsEJDS(EncryptedJSONFile(self.getEncryptionService(), self.file / "repo" / "contributors.ejson"))
    def getUserIfContributor(self, user_id: str | None = None) -> User | None:
        for user in self.getContributorsEJDS().get():
            if user.id == (user_id or Git.getLocalID()):
                return user
    def setup(self) -> None:
        self.uuid = str(createUUID())
        run(self.file, ["git", "init"])
        print(String.repo.createSuccess(formatted=True, file=(self.file / "README.txt").write(README.read())))
        print(String.repo.createSuccess(formatted=True, file=(self.file / "repo").mkdir()))
        print(String.repo.createSuccess(formatted=True, file=(self.file / "repo" / "uuid.txt").write(self.uuid)))
        (KEYS_DIRECTORY / (self.uuid + ".vom")).writeBytes(EncryptionService.newKey())
        print(String.repo.createSuccess(formatted=True, file=EncryptedJSONFile(self.getEncryptionService(), self.file / "repo" / "github.ejson").write({})))
        print(String.repo.createSuccess(formatted=True, file=(self.file / "repo" / "vom.json").write(VOM_JSON.read())))
        print(String.repo.createSuccess(formatted=True, file=(self.file / "implementations").mkdir()))
        print(String.repo.createSuccess(formatted=True, file=(self.file / "implementations" / "master").mkdir()))
        print(String.repo.createSuccess(formatted=True, file=EncryptedJSONFile(self.getEncryptionService(), self.file / "implementations" / "master" / "contributors.ejson").write({
            Git.getLocalID(): {
                "permissions": [],
                "owner": True
            }
        })))
        print(String.repo.createSuccess(formatted=True, file=(self.file / "implementations" / "master" / "commits").mkdir()))
        print(String.repo.createSuccess(formatted=True, file=EncryptedJSONFile(self.getEncryptionService(), self.file / "repo" / "contributors.ejson").write([{
            "username": Git.getLocalUsername(),
            "email": Git.getLocalEmail(),
            "id": Git.getLocalID(),
            "opened": None,
            "owner": True,
            "log": []
        }])))
        contributors: ContributorsEJDS = self.getContributorsEJDS()
        contributors.data[0]["opened"] = self.getImplementations()[0].toDict()
        contributors.write()
    @classmethod
    def make(cls, file: File) -> "Repo":
        (file / ".vom").mkdir()
        return cls(file)