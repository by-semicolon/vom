from .string import String


def promptConfirmation(action: str) -> bool:
    answer: str = "_"
    while answer not in "YyNn":
        try:
            answer = input(String.prmt.format(formatted=True, prompt=String.prmt.confirmation(action=action)))
        except (KeyboardInterrupt, EOFError):
            answer = "n"
            print()
    if answer not in "Yy":
        print(String.prmt.cancelled(formatted=True))
        return False
    return True