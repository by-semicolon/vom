from subprocess import run as spRun

from .file import File


def get(where: File | str, command: str | list[str]) -> str:
    return str(spRun(command, shell=isinstance(command, str), cwd=where.getFullPath() if isinstance(where, File) else where, capture_output=True, text=True))

def run(where: File | str, command: str | list[str]) -> None:
    print(get(where, command).stdout)