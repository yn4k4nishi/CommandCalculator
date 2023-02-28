from commands.command import Command

class ReverseSign(Command):
    def __init__(self, base: str) -> None:
        self.base = base

    def execute(self) -> None:
        if '-' in self.base:
            return self.base[1:]
        else:
            return '-' + self.base