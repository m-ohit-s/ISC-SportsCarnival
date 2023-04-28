class CommunicationProtocol:
    size = int
    REQUEST = "request"
    RESPONSE = "response"
    data = list
    protocol_version = str
    protocol_format = str
    protocol_type = str
    source_ip = str
    source_port = int
    destination_ip = str
    destination_port = int
    headers = dict

    def __init__(self):
        self.size = None
        self.protocol_type = None
        self.data = None
        self.protocol_version = None
        self.protocol_format = None
        self.source_ip = None
        self.source_port = None
        self.destination_ip = None
        self.destination_port = None
        self.headers = None

