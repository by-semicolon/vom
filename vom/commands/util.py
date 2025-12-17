from vom.resources.scripts.file import File
from vom.resources.scripts.string import String


HERE: File = File(__file__)
KEYS_DIRECTORY: File = (HERE / ".." / ".." / "keys")

def util(args: list[str]) -> None:
    command: str = args.pop(0)
    match command:
        case "--clear-keys":
            for file in KEYS_DIRECTORY.getChildren():
                print(String.util.deletingKey(formatted=True, file=file))
                file.delete()