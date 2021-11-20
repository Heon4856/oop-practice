import abc
import inspect
from functools import wraps

from base_policy.base_policy_impl import BasePricingImpl
from base_policy.base_policy_interface import BasePricing
from discount_policy.discount_policy_impl import ParkingZoneDiscount, EarlyReuseDiscount
from discount_policy.discount_policy_interface import BaseDiscount
from policy_checker.base_policy_checker import PolicyCheckerImplement
from policy_checker.discount_policy_checker import DiscountPolicyCheckerImplement
from policy_checker.policy_checker_interface import PolicyChecker


class Repo:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get(self):
        pass


class MySQLRepo(Repo):
    def get(self):
        print('MySQLRepo')


providers = {
        PolicyChecker: DiscountPolicyCheckerImplement,
        BasePricing : BasePricingImpl,
        BaseDiscount : ParkingZoneDiscount
    }

def inject(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = inspect.getfullargspec(func).annotations
        print(annotations)
        for k, v in annotations.items():
            if v in providers:
                kwargs[k] = providers[v]
        print(args)
        print(kwargs)
        return func(*args, **kwargs)

    return wrapper





# if __name__ == '__main__':
#     usecase = Usecase(11)
#     print(usecase)
#     print(usecase.age)
#     print(usecase.repo)
#     usecase.repo.get(usecase)
