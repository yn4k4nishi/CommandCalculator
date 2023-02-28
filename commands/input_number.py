from commands.command import Command

class InputNumber(Command):
    def __init__(self, base: str, input: str) -> None:
        self.base  = base
        self.input = input
    
    def execute(self) -> None:
        return self.base + self.input
