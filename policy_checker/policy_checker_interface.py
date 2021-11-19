from abc import ABC, abstractmethod
from dto import User

class PolicyChecker(ABC):
    @property
    @abstractmethod
    def base_policy(self,deer_area_id,):
        pass


    @property
    @abstractmethod
    def discount_policy(base_charge, deer_area_id, user: User):
        pass


    @property
    @abstractmethod
    def extra_charge_policy(discounted_charge, deer_area_id, user: User):
        pass


    @property
    @abstractmethod
    def exception_policy(extra_charged_price, deer_area_id, user: User):
        pass


    @abstractmethod
    def check_policy(self):
        pass



