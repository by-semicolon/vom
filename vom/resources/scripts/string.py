from .file import File
from .errors import ResourceNotFoundError


HERE: File = File(__file__)
LANG_OPTION: str = (HERE / ".." / ".." / ".." / "language.option").read()
LANG_DIR: File = HERE / ".." / ".." / "lang" / LANG_OPTION

@lambda _: _()
class String:
    def __getattr__(self, category: str) -> str:
        class StringCategory:
            def __getattr__(self, key: str) -> str:
                if not (LANG_DIR / category / (key + ".txt")).exists():
                    if not (LANG_DIR / "misc" / "errorResourceNotFound.txt").exists():
                        raise ResourceNotFoundError(f"{category}.{key}")
                    raise ResourceNotFoundError(String.misc.errorResourceNotFound(stringoption=LANG_OPTION, category=category, key=key))
                return lambda formatted=False, **kwargs: (eval((LANG_DIR / "misc" / "format.txt").read(), {
                    "string": eval("f\"\"\"" + (LANG_DIR / category / (key + ".txt")).read() + "\"\"\"", kwargs),
                    "category": category,
                    "key": key
                }) if formatted else eval("f\"\"\"" + (LANG_DIR / category / (key + ".txt")).read() + "\"\"\"", kwargs))
        return StringCategory()