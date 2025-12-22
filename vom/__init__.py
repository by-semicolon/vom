import sys
from os import system
from copy import deepcopy

from .resources.scripts.file import File
from .resources.scripts.string import String
from .resources.scripts.errors import UnknownCommandError, UsageError
from .resources.scripts.json import JSONFile


HERE: File = File(__file__)

def main() -> None:
    try:
        argv: list[str] = deepcopy(sys.argv)
        if "-v" in argv:
            argv.remove("-v")
        if len(argv) <= 1:
            print(String.misc.info(formatted=True, vom=JSONFile(HERE / ".." / "vom.json")))
            raise UsageError(String.misc.errorNoCommandPassed())
        command: str = argv[1]
        args: list[str] = argv[2:]
        try:
            exec(f"from .commands.{command} import {command}", globals())
        except ImportError:
            raise UnknownCommandError(String.misc.errorUnknownCommand(command=command, commands=(HERE / ".." / "commands").getChildren()))
        globals()[command](args)
    except Exception as error:
        print(String.misc.error(errorname=error.__class__.__name__, errormsg=str(error)))
        if "-v" in sys.argv:
            raise error