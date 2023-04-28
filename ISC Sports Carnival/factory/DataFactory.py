from core.data_operations.JSONData import JSONData


class DataFactory:

    @staticmethod
    def get_input_operator(data_format: str):
        if data_format.lower().strip() == "json":
            return JSONData()

    @staticmethod
    def get_output_operator(data_format: str):
        if data_format.lower().strip() == "json":
            return JSONData()


