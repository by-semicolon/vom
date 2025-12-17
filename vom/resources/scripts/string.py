from vom.resources.scripts.file import File
from vom.resources.scripts.errors import ResourceNotFoundError


HERE: File = File(__file__)
GALLERY: str = (HERE / ".." / ".." / ".." / "use.gallery").read()
STRINGS_DIR: File = HERE / ".." / ".." / "public" / GALLERY

@lambda _: _()
class String:
    def __getattr__(self, category: str) -> str:
        class StringCategory:
            def __getattr__(self, key: str) -> str:
                try:
                    return lambda formatted=False, **kwargs: (eval((STRINGS_DIR / "misc" / "format.txt").read(), {
                        "string": eval("f\"\"\"" + (STRINGS_DIR / category / (key + ".txt")).read() + "\"\"\"", kwargs),
                        "category": category,
                        "key": key
                    }) if formatted else eval("f\"\"\"" + (STRINGS_DIR / category / (key + ".txt")).read() + "\"\"\"", kwargs))
                except FileNotFoundError:
                    raise ResourceNotFoundError(String.misc.errorResourceNotFound(gallery=GALLERY, category=category, key=key))
        return StringCategory()