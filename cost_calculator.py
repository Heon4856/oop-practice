from base_policy.base_policy_interface import BasePricing
from exception_policy.exception_policy_interface import BaseException
from extra_charge_policy.extra_charge_policy_interface import BaseExtraCharge
from policy_checker.policy_checker_interface import PolicyChecker
from injectors.decorators import inject_for_policy_check
from typing import List
from discount_policy.discount_policy_interface import BaseDiscount


class CostCalculator:
    @inject_for_policy_check
    def __init__(self, user, policyChecker: PolicyChecker, base_discounts: List[BaseDiscount],
                 base_extra_charges: List[BaseExtraCharge], base_exceptions: List[BaseException],
                 base_pricings: List[BasePricing]):

        self.BaseExtraCharge = BaseExtraCharge
        self.user = user
        self.deer_area_id = 1
        self.charging_policy = policyChecker
        self.base_discounts = base_discounts
        self.base_extra_charges = base_extra_charges
        self.base_exceptions = base_exceptions
        self.base_pricings = base_pricings

    def calculate(self):
        base_discount = self.charging_policy(self.base_discounts)
        base_extra_charges = self.charging_policy(self.base_extra_charges)
        base_exception = self.charging_policy(self.base_exceptions)
        base_pricing = self.charging_policy(self.base_pricings)

        print(base_discount.policy_check(self.user))
        print(base_extra_charges.policy_check(self.user))
        print(base_exception.policy_check(self.user))
        print(base_pricing.policy_check(self.user))

        return base_exception


if __name__ == "__main__":
    import datetime
    from dto import User

    user = User()
    user.use_end_lat = 1
    user.use_end_lng = 1
    user.use_deer_name = 1
    user.use_start_at = datetime.datetime.now()
    user.use_end_at = datetime.datetime.now() + datetime.timedelta(minutes=10)
    costCalculator = CostCalculator(user)
    print(costCalculator.calculate())
