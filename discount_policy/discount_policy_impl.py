from discount_policy.discount_policy_interface import BaseDiscount
from dto import User
from const import PARKING_ZONE_DISCOUNT_RATE


class ParkingZoneDiscount(BaseDiscount):

    def calculate_discount_amount(self, user: User) -> int:
        before_discount = self.basic_rate + self.per_minute_rate * (user.use_end_at - user.use_start_at)
        self.discount_amount = before_discount * PARKING_ZONE_DISCOUNT_RATE
        return self.discount_amount

    def calculate_after_discount(self, user: User, before_fare) -> int:
        return before_fare - self.calculate_discount_amount(self,user)


class EarlyReuseDiscount(BaseDiscount):

    def calculate_discount_amount(self, user: User) -> int:
        print(self.basic_rate)
        return self.basic_rate

    def calculate_after_discount(self, user: User, before_fare: int) -> int:
        return before_fare - self.calculate_discount_amount(user )
