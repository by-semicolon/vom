from subprocess import run as spRun

from vom.resources.scripts.file import File


def get(where: File | str, command: str) -> str:
    return spRun(command, shell=isinstance(command, str), cwd=where.getFullPath() if isinstance(where, File) else where, capture_output=True, text=True)

def run(where: File | str, command: str) -> None:
    print(get(where, command).stdout)