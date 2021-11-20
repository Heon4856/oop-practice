from policy_checker.policy_checker_interface import PolicyChecker
from base_policy.base_policy_interface import BasePricing
from injectors.decorators import inject


class CostCalculator:
    @inject
    def __init__(self, user, policyChecker: PolicyChecker, basePricing : BasePricing) :
        self.user = user
        self.deer_area_id = 1
        self.charging_policy = policyChecker
        self.basePricing = basePricing

    def calculate(self):
        base_policy = self.charging_policy.base_policy(PolicyChecker, self.deer_area_id, self.basePricing)
        print(base_policy.basic_rate, base_policy.per_minute_rate)
        charge_calculating: int = base_policy.calculate_fee(base_policy, self.user.use_end_at - self.user.use_start_at)

        discount_polices = self.charging_policy.discount_policy(self, self.deer_area_id, self.user)
        print(discount_polices)

        for policy in discount_polices:
            charge_calculating: int = policy.calculate_after_discount(self.user, charge_calculating)

        extra_charged_policies: list = self.charging_policy.extra_charge_policy(self, self.deer_area_id, self.user)
        for policy in extra_charged_policies:
            charge_calculating: int = policy.calculate_after_extra_charge(policy, self.user, charge_calculating)

        if self.charging_policy.exception_policy(self, self.user):
            charge_calculating: int = self.charging_policy.exception_policy.calculate_exception(charge_calculating)

        return charge_calculating


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
    print(costCalculator.charging_policy)
    print(costCalculator.calculate())
