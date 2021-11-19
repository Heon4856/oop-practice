from abc import ABC, abstractmethod
from dto import User

class BaseExtraCharge(ABC):

    @abstractmethod
    def calculate_extra_charge_amount(self,user):
        pass


    @abstractmethod
    def calculate_after_extra_charge(self, before_fare: int):
        pass



