from vom.resources.scripts.file import File
from vom.resources.scripts.string import String
from vom.resources.scripts.errors import NotARepoError
from vom.resources.scripts.system import run
from vom.resources.scripts.implementation import Implementation

class Repo:
    def __init__(self, parent: File):
        self.parent: File = parent
        self.file: File = self.parent / String.repo.name()
        if not self.file.exists():
            raise NotARepoError(String.repo.errorNotARepo(file=self.parent))
        self.implementations: list[Implementation] = []
    def setup(self) -> None:
        run(self.file, ["git", "init"])
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.readMeFile()).write(String.repo.readMeContent())))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.infoDir()).mkdir()))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.contributorsJson()).write("{}")))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.githubJson()).write("{}")))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.vomJson()).write("{}")))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.implementationsDir()).mkdir()))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.implementationDir(implementation="master")).mkdir()))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.implementationInfoDir(implementation="master")).mkdir()))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.implementationContributorsJson(implementation="master")).write("{}")))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.implementationRulesJson(implementation="master")).write("{}")))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.commitsDir(implementation="master")).mkdir()))
        print(String.repo.createSuccess(formatted=True, file=(self.file / String.repo.trackDir(implementation="master")).mkdir()))
    def fetchImplementations(self) -> None: 
        for name in (self.file / "implementations").getChildren():
            self.implementations.append(Implementation(self.file / "implementations" / name))
    @classmethod
    def make(cls, file: File) -> "Repo":
        (file / String.repo.name()).mkdir()
        return cls(file)