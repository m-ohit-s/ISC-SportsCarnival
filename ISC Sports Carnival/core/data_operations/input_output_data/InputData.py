from factory.DataFactory import DataFactory


class InputData:

    @staticmethod
    def get_file_object(location: str):
        try:
            if location is None:
                raise FileNotFoundError
            data = open(location, 'r')
            return data
        except FileNotFoundError as f:
            print("File not found. Check command again")
            return None

    @staticmethod
    def read_file(data):
        try:
            if data is None:
                raise FileNotFoundError
        except FileNotFoundError as e:
            return data
        except AttributeError as e:
            return data
        return data.read()

    @staticmethod
    def process_data(data, data_format: str):
        data_factory = DataFactory()
        operator = data_factory.get_input_operator(data_format)
        new_data = operator.build_input_data(data)
        return new_data

