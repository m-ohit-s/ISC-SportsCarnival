from communication_protocol.ICSRequest import ICSRequest
from communication_protocol.ICSResponse import ICSResponse
from model.Protocol import Protocol
from model.ProtocolIpPort import ProtocolIpPort
from utils.custom_logger.CustomLogger import CustomLogger

logger = CustomLogger()


class RequestResponseHandler:

    @staticmethod
    def create_request(
            size: int,
            source: ProtocolIpPort,
            destination: ProtocolIpPort,
            local_data: list,
            protocol: Protocol,
            headers: dict
    ) -> ICSRequest:
        local_request = ICSRequest()
        local_request.size = size
        local_request.data = local_data
        local_request.protocol_format = protocol.protocol_format
        local_request.protocol_version = protocol.protocol_version
        local_request.source_ip = source.ip
        local_request.source_port = source.port
        local_request.destination_ip = destination.ip
        local_request.destination_port = destination.port
        local_request.headers = headers
        logger.debug("Creating request object")
        return local_request

    @staticmethod
    def create_response(
            processed_data,
            request: ICSRequest,
    ):
        response = ICSResponse()
        response.size = request.size
        response.protocol_version = request.protocol_version
        response.data = processed_data
        response.source_ip = request.source_ip
        response.source_port = request.source_port
        response.destination_ip = request.destination_ip
        response.destination_port = request.destination_port
        response.protocol_format = request.protocol_format
        logger.debug("Creating response object")
        return response
