from commands.command import Command

class Clear(Command):
    def __init__(self) -> None:
        pass

    def execute(self) -> None:
        return '0'
