import json

from core.data_operations.IData import IData
from utils.custom_logger.CustomLogger import CustomLogger
from utils.json_encoder.ObjectEncoder import ObjectEncoder


class JSONData(IData):

    def build_input_data(self, input_data) -> dict:
        dictionary_data = json.loads(input_data)
        return dictionary_data

    def build_output_data(self, processed_data: dict) -> str:
        json_data = json.dumps(processed_data, indent=4, cls=ObjectEncoder)
        return json_data



