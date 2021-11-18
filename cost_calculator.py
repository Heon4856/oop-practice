from check_policy import CheckPolicy
from calculate_rule import Calculating

class CostCalculator:

    def __init__(self, user):
        self.user = user
        self.deer_area_id = find( user.deer_name)
        self.charging_policy= CheckPolicy( self.deer_area_id )

    def calculate(self):
        base_charge = self.charging_policy.base_policy(self.deer_area_id, user)
        discounted_charge = self.charging_policy.discount_policy(base_charge,self.deer_area_id, user)
        extra_charged_price = self.charging_policy.extra_charge_policy(discounted_charge,self.deer_area_id, user )
        last_price = self.charging_policy.exception_policy(extra_charged_price, self.deer_area_id, user)

        return last_price







