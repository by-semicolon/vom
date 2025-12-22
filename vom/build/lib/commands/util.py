from ..resources.scripts.json import JSONFile
from ..resources.scripts.file import File
from ..resources.scripts.prompt import promptConfirmation
from ..resources.scripts.string import String
from ..resources.scripts.errors import UnknownCommandError, UsageError


HERE: File = File(__file__)
KEYS_DIRECTORY: File = (HERE / ".." / ".." / "keys")
STRING_OPTION: File = (HERE / ".." / ".." / "string.option")

def util(args: list[str]) -> None:
    if len(args) <= 1:
        print(String.misc.info(formatted=True, vom=JSONFile(HERE / ".." / "vom.json")))
        raise UsageError(String.misc.errorNoCommandPassed())
    command: str = args.pop(0)
    match command:
        case "--clear-keys":
            if promptConfirmation(String.util.clearKeysConfirmation()):
                for file in KEYS_DIRECTORY.getChildren():
                    print(String.util.deletingKey(formatted=True, file=file))
                    file.delete()
        case "--reset-string-option":
            STRING_OPTION.write("vom.standard")
            print(String.util.resetStringOptionSuccess())
        case _:
            raise UnknownCommandError(String.misc.errorUnknownCommand(command=command))