import pathlib

from .file import File


class VomIgnore:
    def __init__(self, file: File | None = None) -> None:
        self.file: File = file or File(".vomignore")
    def parse(self) -> list[File] | None:
        if not self.file.exists():
            return
        ignore: list[File] = []
        for line in self.file.read().split("\n"):
            line = line.strip()
            if line.startswith("#"):
                continue
            ignore += [File(path.name) for path in pathlib.Path(".").glob(line)]
        return ignore
    def isIgnored(self, file: File) -> bool:
        if not self.file.exists():
            return False
        return file in self.parse()