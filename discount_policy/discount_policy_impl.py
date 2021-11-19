from discount_policy_interface import BaseDiscount
from dto import User
from const import PARKING_ZONE_DISCOUNT_RATE


class ParkingZoneDiscount(BaseDiscount):

    def calculate_discount_amount(self, user: User)->int:
        before_discount = self.basic_rate + self.per_minute_rate * (user.use_end_at - user.use_start_at)
        self.before_discount = before_discount
        print(before_discount)
        self.discount_amount = before_discount * PARKING_ZONE_DISCOUNT_RATE
        return self.discount_amount

    def calculate_after_discount(self)-> int:
        return self.before_discount - self.discount_amount


class EarlyReuseDiscount(BaseDiscount):

    def calculate_discount_amount(self, user: User)-> int:
        before_discount = self.basic_rate + self.per_minute_rate * (user.use_end_at - user.use_start_at)
        self.before_discount = before_discount
        self.discount_amount = self.basic_rate
        return self.basic_rate

    def calculate_after_discount(self)-> int:
        return self.before_discount - self.discount_amount

