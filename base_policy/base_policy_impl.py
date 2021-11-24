from base_policy.base_policy_interface import BasePricing
import datetime
from dto import User


from const import base_policy_const
from mock_db import find_base_pricing


class BasePricingImplement(BasePricing):

    def base_price_setting(self, deer_area_id: int):
        self.basic_rate = base_policy_const[deer_area_id]["basic_rate"]
        self.per_minute_rate = base_policy_const[deer_area_id]["per_minute_rate"]

    def calculate_fee(self, minute) -> int:
        minute = str(minute).split(":")[1]
        minute = int(minute)
        return self.basic_rate + minute * self.per_minute_rate

    def policy_check(self, user: User) -> bool:
        if find_base_pricing():
            return True
        return False