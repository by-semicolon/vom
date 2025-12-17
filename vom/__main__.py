import sys
from os import system
from copy import deepcopy

from vom.resources.scripts.file import File
from vom.resources.scripts.string import String
from vom.resources.scripts.errors import UnknownCommandError, UsageError
from vom.resources.scripts.json import JSONFile


HERE: File = File(__file__)

def main() -> None:
    argv: list[str] = deepcopy(sys.argv)
    if "-v" in argv:
        argv.remove("-v")
    if len(argv) < 2:
        print(String.misc.info(formatted=True, vom=JSONFile(HERE / ".." / "vom.json")))
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
    print(String.misc.error(errorname=error.__class__.__name__, errormsg=str(error)))
    if "-v" in sys.argv:
        raise error