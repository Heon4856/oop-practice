from abc import ABC, abstractmethod


class BaseDiscount(ABC):

    @property
    def basic_rate(self):
        return self._basic_rate

    @basic_rate.setter
    def basic_rate(self):
        return self._basic_rate

    @property
    def per_minute_rate(self):
        return self._per_minute_rate

    @per_minute_rate.setter
    def per_minute_rate(self):
        return self._per_minute_rate

    @abstractmethod
    def calculate_discount_amount(self, user):
        pass


    @abstractmethod
    def calculate_after_discount(self):
        pass



