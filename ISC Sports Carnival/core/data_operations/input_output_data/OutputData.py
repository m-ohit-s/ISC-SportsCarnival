from factory.DataFactory import DataFactory


class OutputData:

    @staticmethod
    def write_data(location: str, data_format: str, data):
        with open(location, "w") as outfile:
            data_factory = DataFactory()
            operator = data_factory.get_output_operator(data_format)
            new_data = operator.build_output_data(data)
            outfile.write(new_data)
            outfile.flush()
