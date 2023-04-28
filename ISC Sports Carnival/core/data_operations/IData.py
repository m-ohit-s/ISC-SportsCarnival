import json
from abc import ABCMeta, abstractmethod


class IData(metaclass=ABCMeta):

    @abstractmethod
    def build_input_data(self, data) -> dict:
        pass

    @abstractmethod
    def build_output_data(self, data) -> str:
        pass
