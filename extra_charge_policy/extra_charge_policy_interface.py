from abc import ABC, abstractmethod
from dto import User

class BaseExtraCharge(ABC):
    @property
    def user(self):
        return f"basic_rate = {self._user}"

    @user.setter
    def user(self):
        return self._user


    @property
    @abstractmethod
    def extra_charge_amount(self):
        pass


    @abstractmethod
    def calculate_after_extra_charge(self, before_fare):
        pass



