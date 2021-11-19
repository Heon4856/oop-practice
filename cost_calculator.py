from policy_checker.check_policy_Impl import CheckPolicy


class CostCalculator:

    def __init__(self, user):
        self.user = user
        self.deer_area_id = 1
        self.charging_policy= CheckPolicy( user , self.deer_area_id )

    def calculate(self):
        base_policy = self.charging_policy.base_policy
        charge_calculating = base_policy.calculate_fee(self.user.use_end_at - self.user.use_start_at )

        discount_polices = self.charging_policy.discount_policy

        for policy in discount_polices:
            charge_calculating = policy.calculate_fee(self.user)


        extra_charged_policies = self.charging_policy.extra_charge_policy
        for policy in extra_charged_policies:
            charge_calculating = policy.calculate_fee(charge_calculating)


        if self.charging_policy.exception_policy:
            charge_calculating = self.charging_policy.exception_policy.calculate_exception(charge_calculating)

        return charge_calculating







