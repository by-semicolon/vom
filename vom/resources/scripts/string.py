from vom.resources.scripts.file import File


HERE: File = File(__file__)
LANG: str = (HERE / ".." / ".." / ".." / ".lang").read()
STRINGS_DIR: File = HERE / ".." / ".." / "localization" / LANG

@lambda _: _()
class String:
    def __getattr__(self, category: str) -> str:
        class StringCategory:
            def __getattr__(self, key: str) -> str:
                return lambda formatted=False, **kwargs: (eval((STRINGS_DIR / "misc" / "format.txt").read(), {
                    "string": eval("f\"\"\"" + (STRINGS_DIR / category / (key + ".txt")).read() + "\"\"\"", kwargs),
                    "category": category,
                    "key": key
                }) if formatted else eval("f\"\"\"" + (STRINGS_DIR / category / (key + ".txt")).read() + "\"\"\"", kwargs))
        return StringCategory()