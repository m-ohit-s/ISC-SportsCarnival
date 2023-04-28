from communication_protocol.CommunicationProtocol import CommunicationProtocol


class ICSResponse(CommunicationProtocol):
    __header_parameters = {}
    __STATUS = "status"
    __CODE = "code"
    __ERROR_MESSAGE = "message"

    def __init__(self):
        super().__init__()
        self.protocol_type = self.RESPONSE
        self.__header_parameters[self.__STATUS] = ""
        self.__header_parameters[self.__CODE] = ""
        self.headers = self.__header_parameters

    def get_error_message(self):
        self.get_value(self.__ERROR_MESSAGE)

    def set_error_message(self, error_message):
        self.set_value(self.__ERROR_MESSAGE, error_message)

    def get_value(self, key):
        headers = super().headers
        return headers.get(key, default=None)

    def set_value(self, key, value):
        self.__header_parameters[key] = value
        super().headers = self.__header_parameters


