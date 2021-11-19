from discount_policy_interface import BaseDiscount
from dto import User
from const import PARKING_ZONE_DISCOUNT_RATE


class ParkingZoneDiscount(BaseDiscount):

    def discount_amount(self, user: User)->int:
        before_discount = self.basic_rate + self.per_minute_rate * (user.use_start_at - user.use_end_at)
        self.before_discount = before_discount
        return before_discount * PARKING_ZONE_DISCOUNT_RATE

    def calculate_after_discount(self)-> int:
        return self.before_discount - self.discount_amount


class EarlyReuseDiscount(BaseDiscount):

    def discount_amount(self, user: User)-> int:
        before_discount = self.basic_rate + self.per_minute_rate * (user.use_start_at - user.use_end_at)
        self.before_discount = before_discount
        return self.basic_rate

    def calculate_after_discount(self)-> int:
        return self.before_discount - self.discount_amount
