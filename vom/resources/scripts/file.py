import os, shutil
from datetime import datetime


class File:
    def __init__(self, path: "str | File | None" = None) -> None:
        self.path: str = path.path if isinstance(path, File) else (path if isinstance(path, str) else os.getcwd())
    def read(self) -> str:
        with open(self.path) as file:
            return file.read()
    def write(self, content: str) -> "File":
        with open(self.path, "w") as file:
            file.write(content)
        return self
    def readBytes(self) -> bytes:
        with open(self.path, "rb") as file:
            return file.read()
    def writeBytes(self, content: bytes) -> "File":
        with open(self.path, "wb") as file:
            file.write(content)
        return self
    def getFullPath(self) -> str:
        return os.path.abspath(self.path)
    def getFileName(self) -> str:
        return os.path.basename(self.path)
    def getFileExtension(self) -> str:
        return os.path.splitext(self.path)[1]
    def getFileSize(self) -> int:
        return os.path.getsize(self.path)
    def getFileCreationTime(self) -> datetime:
        return datetime.fromtimestamp(os.path.getctime(self.path))
    def getFileModificationTime(self) -> datetime:
        return datetime.fromtimestamp(os.path.getmtime(self.path))
    def getParent(self) -> "File":
        return File(os.path.dirname(self.path))
    def getChildren(self) -> "list[File]":
        return [(self / item) for item in os.listdir(self.getFullPath())]
    def __truediv__(self, other: "str | int | File") -> "File":
        if other == "..":
            return self.getParent()
        return File(os.path.join(self.path, str(other.path if isinstance(other, File) else other)))
    def getTree(self, exclude: list[str], *, tree_location: str = "") -> "list[tuple[str, File]]":
        files: list[tuple[str, File]] = []
        for file in self.getChildren():
            if file.getFileName() in exclude:
                continue
            elif file.isFile():
                files.append((tree_location.strip("/"), file))
            else:
                files += file.getTree(tree_location=f"{tree_location}/{self.getFileName()}", exclude=[])
        return files
    def exists(self) -> bool:
        return os.path.exists(self.path)
    def mkdir(self) -> "File":
        os.makedirs(self.path, exist_ok=True)
        return self
    def copy(self, destination: "File") -> "File":
        if self.isDirectory():
            shutil.copytree(self.path, destination.path)
        elif self.isFile():
            shutil.copy2(self.path, destination.path)
        return self
    def delete(self) -> "File":
        if self.isDirectory():
            shutil.rmtree(self.path)
        elif self.isFile():
            os.remove(self.path)
        return self
    def isDirectory(self) -> bool:
        return os.path.isdir(self.path)
    def isFile(self) -> bool:
        return os.path.isfile(self.path)
    def isSymbolicLink(self) -> bool:
        return os.path.islink(self.path)
    def isExecutable(self) -> bool:
        return os.path.isexecutable(self.path)
    def isReadable(self) -> bool:
        return os.path.isreadable(self.path)
    def isWritable(self) -> bool:
        return os.path.iswritable(self.path)
    def __str__(self) -> str:
        return str(self.path)
    def __repr__(self) -> str:
        return f"File('{self.path}')"
    def __eq__(self, other: "File | str") -> bool:
        return self.getFullPath() == (other.getFullPath() if isinstance(other, File) else other)