from .string import String


def promptYN(prompt: str) -> bool:
    answer: str = input(String.prmt.format(prompt=prompt))
    return answer
def promptConfirmation(action: str) -> bool:
    answer: str = "_"
    while answer not in "YyNn":
        try:
            answer = promptYN(String.prmt.confirmation(action=action))
        except (KeyboardInterrupt, EOFError):
            answer = "n"
            print()
    if answer not in "Yy":
        print(String.prmt.cancelled(formatted=True))
        return False
    return True