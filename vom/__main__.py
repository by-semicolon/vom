import sys
from os import system
from copy import deepcopy

from vom.resources.scripts.file import File
from vom.resources.scripts.string import String
from vom.resources.scripts.errors import UnknownCommandError, UsageError


HERE: File = File(__file__)

def main() -> None:
    argv: list[str] = deepcopy(sys.argv)
    if "-v" in argv:
        argv.remove("-v")
    if len(argv) < 2:
        raise UsageError(String.misc.errorNoCommandPassed())
    command: str = argv[1]
    args: list[str] = argv[2:]
    try:
        exec(String.misc.importCommandStatement(command=command, args=args), globals())
    except ImportError:
        raise UnknownCommandError(String.misc.errorUnknownCommand(command=command, commands=(HERE / ".." / "commands").getChildren()))
    globals()[command](args)
try:
    main()
except Exception as error:
    new_name: str = ""
    for char in error.__class__.__name__.removesuffix("Error"):
        if char.isupper():
            new_name += " "
        new_name += char.lower()
    print(String.misc.error(errorname=new_name.strip(), errormsg=str(error)))
    if "-v" in sys.argv:
        raise error