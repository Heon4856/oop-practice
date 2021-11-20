from abc import ABC, abstractmethod
from dto import User
from base_policy.base_policy_interface import BasePricing


class PolicyChecker(ABC):
    @abstractmethod
    def base_policy(self, deer_area_id, base_pricing:BasePricing):
        pass

