from ..resources.scripts.file import File


HERE: File = File(__file__)
README: File = (HERE / ".." / ".." / "README.txt")

def help(args: list[str]) -> None:
    print(README.read())