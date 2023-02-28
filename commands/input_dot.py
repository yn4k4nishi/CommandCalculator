from commands.command import Command

class InputDot(Command):
    def __init__(self, base: str) -> None:
        self.base = base

    def execute(self) -> None:
        if '.' in self.base:
            return self.base
        else:
            return self.base + '.'
        