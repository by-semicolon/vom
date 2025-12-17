from uuid import uuid4 as createUUID, getnode as getNode

from vom.resources.scripts.file import File
from vom.resources.scripts.git import Git
from vom.resources.scripts.json import JSONFile
from vom.resources.scripts.string import String
from vom.resources.scripts.errors import NotARepoError
from vom.resources.scripts.system import run
from vom.resources.scripts.implementation import Implementation
from vom.resources.scripts.encryption import EncryptionService
from vom.resources.scripts.dataset import ContributorsEJDS


HERE: File = File(__file__)
KEYS_DIRECTORY: File = (HERE / ".." / ".." / ".." / "keys")
VOM_JSON: File = (HERE / ".." / ".." / ".." / "vom.json")

class Repo:
    def __init__(self, parent: File):
        self.parent: File = parent
        self.file: File = self.parent / String.repo.name()
        if not self.file.exists():
            raise NotARepoError(String.repo.errorNotARepo(file=self.parent))
        self.implementations: list[Implementation] | None = None
        self.uuid: str | None = None
        self.es: EncryptionService | None = None
        self.contributors: ContributorsEJDS | None = None
    def fetchData(self) -> None:
        self.implementations = []
        for name in (self.file / "implementations").getChildren():
            self.implementations.append(Implementation(self.file / "implementations" / name))
        self.uuid = (self.file / String.repo.uuidFile()).read()
        self.es = EncryptionService((KEYS_DIRECTORY / (self.uuid + ".vom")).read())
        self.contributors = ContributorsEJDS(self.es, (self.file / String.repo.contributorsJson()), JSONFile(self.file / String.repo.contributorsJson()).read())
    def setup(self) -> None:
        self.uuid = str(createUUID())
        run(self.file, ["git", "init"])
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.readMeFile()).write(String.repo.readMeContent())))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.uuidFile()).write(self.uuid)))
        (KEYS_DIRECTORY / (self.uuid + ".vom")).writeBytes(EncryptionService.newKey())
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.infoDir()).mkdir()))
        print(String.repo.createSuccess(formatted=True, file=JSONFile(self.file / String.repo.contributorsJson()).write([{
            "username": Git.getLocalUsername(),
            "email": Git.getLocalEmail(),
            "id": str(getNode())
        }])))
        print(String.repo.createSuccess(formatted=True, file=JSONFile(self.file / String.repo.githubJson()).write({})))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.vomJson()).write(VOM_JSON.read())))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.implementationsDir()).mkdir()))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.implementationDir(implementation="master")).mkdir()))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.implementationInfoDir(implementation="master")).mkdir()))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.implementationContributorsJson(implementation="master")).write("{}")))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.implementationRulesJson(implementation="master")).write("{}")))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.commitsDir(implementation="master")).mkdir()))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.trackDir(implementation="master")).mkdir()))
        self.fetchData()
    @classmethod
    def make(cls, file: File) -> "Repo":
        (file / String.repo.name()).mkdir()
        return cls(file)