import abc


class Service(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, input):
        return NotImplementedError()