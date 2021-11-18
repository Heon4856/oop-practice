from abc import ABC, abstractmethod
from dto import User

class BaseException(ABC):

    @property
    def basic_rate(self):
        return f"basic_rate = {self._basic_rate}"

    @basic_rate.setter
    def basic_rate(self):
        return self._basic_rate

    @property
    def per_minute_rate(self):
        return f"per_minute_rate = {self._per_minute_rate}"

    @per_minute_rate.setter
    def per_minute_rate(self):
        return self._per_minute_rate


    @property
    @abstractmethod
    def exception_change_amount(self,user: User):
        pass


    @abstractmethod
    def calculate_exception(self, before_fare):
        pass



