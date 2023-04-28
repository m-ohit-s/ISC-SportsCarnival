from communication_protocol.CommunicationProtocol import CommunicationProtocol


class ICSRequest(CommunicationProtocol):
    __header_parameters = {}
    __METHOD = "method"

    def __init__(self):
        super().__init__()
        self.protocol_type = self.REQUEST
        self.__header_parameters[self.__METHOD] = ""
        self.headers = self.__header_parameters


    @classmethod
    def from_dict(cls, data):
        req = cls()
        req.size = data['size']
        req.data = data['data']
        req.protocol_version = data['protocol_version']
        req.protocol_format = data['protocol_format']
        req.protocol_type = data['protocol_type']
        req.source_ip = data['source_ip']
        req.source_port = data['source_port']
        req.destination_ip = data['destination_ip']
        req.destination_port = data['destination_port']
        req.headers = data['headers']
        return req