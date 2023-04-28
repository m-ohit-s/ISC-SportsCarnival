class CreateTeamExceptions:
    class InvalidData(Exception):
        def __init__(self, error_type="Error", message="Invalid Data", description="", error_code=1):
            super().__init__(message)
            self.error_type = error_type
            self.message = message
            self.description = description
            self.error_code = error_code

    class IncorrectDataFormat(Exception):
        def __init__(self, error_type="Error", message="Incorrect Data Format", description="", error_code=2):
            super().__init__(message)
            self.error_type = error_type
            self.message = message
            self.description = description
            self.error_code = error_code
