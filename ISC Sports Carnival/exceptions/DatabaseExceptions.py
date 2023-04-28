class DatabaseExceptions:
    class SingletonInstanceException(Exception):
        def __init__(self, message="Cannot create multiple instances of DatabaseConnection class."
                                   " Use get_instance() method to get the instance."):
            super().__init__(message)
            self.message = message
