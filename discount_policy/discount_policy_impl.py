from discount_policy.discount_policy_interface import BaseDiscount
from dto import User
from const import PARKING_ZONE_DISCOUNT_RATE, base_policy_const, REUSE_TIMEDELTA
from mock_db import find_parking_zone, find_user_last_use
from utils import calculate_distance


class ParkingZoneDiscount(BaseDiscount):

    def calculate_discount_amount(self, user: User) -> int:
        before_discount = self.basic_rate + self.per_minute_rate * (user.use_end_at - user.use_start_at)
        self.discount_amount = before_discount * PARKING_ZONE_DISCOUNT_RATE
        return self.discount_amount

    def calculate_after_discount(self, user: User, before_fare) -> int:
        return before_fare - self.calculate_discount_amount(self,user)

    def policy_check(self, user: User) -> bool:
        # if parkingzone.parkingzone_radius < calculate_distance(user_coods, parkingzone_coods)
        parkingzone = find_parking_zone()
        user_coods = (user.use_end_lng, user.use_end_lat)
        parkingzone_coods = (parkingzone.parkingzone_center_lng, parkingzone.parkingzone_center_lat)
        calculate_distance(user_coods, parkingzone_coods)
        if parkingzone.parkingzone_radius < calculate_distance(user_coods, parkingzone_coods):
            self.basic_rate = base_policy_const[1]["basic_rate"]
            self.per_minute_rate = base_policy_const[1]["per_minute_rate"]
            return True
        return False


class EarlyReuseDiscount(BaseDiscount):

    def calculate_discount_amount(self, user: User) -> int:
        return self.basic_rate

    def calculate_after_discount(self, user: User, before_fare: int) -> int:
        return before_fare - self.calculate_discount_amount(self, user )

    def policy_check(self, user: User) -> bool:
        if user.use_start_at - find_user_last_use() < REUSE_TIMEDELTA:
            self.basic_rate = base_policy_const[1]["basic_rate"]
            self.per_minute_rate = base_policy_const[1]["per_minute_rate"]
            return True
        return False