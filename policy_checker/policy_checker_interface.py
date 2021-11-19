from abc import ABC, abstractmethod
from dto import User
from base_policy.base_policy_interface import BasePricing

class PolicyChecker(ABC):

    @abstractmethod
    def base_policy(self, deer_area_id, base_pricing:BasePricing):
        pass

    @abstractmethod
    def discount_policy(base_charge, deer_area_id, user: User):
        pass

    @abstractmethod
    def extra_charge_policy(discounted_charge, deer_area_id, user: User):
        pass

    @abstractmethod
    def exception_policy(extra_charged_price, deer_area_id, user: User):
        pass

    @abstractmethod
    def check_policy(self):
        pass
