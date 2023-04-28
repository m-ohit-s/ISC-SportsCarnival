class Error:
    def __init__(self, type_of_error: str, message: str, description):
        self.type: str = type_of_error
        self.message: str = message
        self.description: str = description

    def __eq__(self, other):
        if isinstance(other, Error):
            return self.type == other.type and\
                self.message == other.message and\
                self.description == other.description
        return False
