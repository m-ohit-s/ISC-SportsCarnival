class CommandException:
    class InvalidCommand(Exception):
        def __init__(self, message="Invalid Command"):
            super().__init__(message)
            self.message = message
