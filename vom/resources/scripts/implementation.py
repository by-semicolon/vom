from vom.resources.scripts.file import File
from vom.resources.scripts.string import String


class Implementation:
    def __init__(self, file: File) -> None:
        self.file: File = file
        self.name: str = file.getFileName()