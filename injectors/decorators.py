import abc
import inspect
from functools import wraps
from typing import List



def inject_for_policy_check(func):

    from policy_checker.discount_policy_checker import DiscountPolicyCheckerImplement
    from policy_checker.policy_checker_interface import PolicyChecker
    from discount_policy.discount_policy_impl import ParkingZoneDiscount, EarlyReuseDiscount
    from discount_policy.discount_policy_interface import BaseDiscount
    from extra_charge_policy.extra_charge_policy_interface import BaseExtraCharge
    from extra_charge_policy.extra_charge_policy_impl import OutsideDistrict
    from extra_charge_policy.extra_charge_policy_impl import AtForbiddenDistrict
    from exception_policy.exception_policy_interface import BaseException
    from exception_policy.exception_policy_impl import QuickReturnPolicy

    from base_policy.base_policy_interface import BasePricing
    from base_policy.base_policy_impl import BasePricingImpl
    providers = {
        PolicyChecker: DiscountPolicyCheckerImplement,
        List[BaseDiscount]: [ParkingZoneDiscount, EarlyReuseDiscount],
        List[BaseExtraCharge] : [OutsideDistrict, AtForbiddenDistrict],
        List[BaseException] : [ QuickReturnPolicy],
        List[BasePricing] : [BasePricingImpl]
    }

    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = inspect.getfullargspec(func).annotations
        for k, v in annotations.items():
            if v in providers:
                kwargs[k] = providers[v]

        return func(*args, **kwargs)

    return wrapper


def inject(func):
    # from base_policy.base_policy_impl import BasePricingImpl
    # from base_policy.base_policy_interface import BasePricing

    providers = {
        # BasePricing  : BasePricingImpl,
    }

    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = inspect.getfullargspec(func).annotations
        for k, v in annotations.items():
            if v in providers:
                kwargs[k] = providers[v]

        return func(*args, **kwargs)

    return wrapper
