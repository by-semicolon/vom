import os, shutil
from datetime import datetime


class File:
    def __init__(self, path: "str | File") -> None:
        self.path: str = path.path if isinstance(path, File) else path
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
        return os.path.getctime(self.path)
    def getFileModificationTime(self) -> datetime:
        return os.path.getmtime(self.path)
    def getParent(self) -> str:
        return File(os.path.dirname(self.path))
    def getChildren(self) -> "list[File]":
        return [(self / item) for item in os.listdir(self.getFullPath())]
    def __truediv__(self, other: "str | File") -> "File":
        if other == "..":
            return self.getParent()
        return File(os.path.join(self.path, other.path if isinstance(other, File) else other))
    def exists(self) -> bool:
        return os.path.exists(self.path)
    def mkdir(self) -> None:
        os.makedirs(self.path, exist_ok=True)
        return self
    def delete(self) -> None:
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