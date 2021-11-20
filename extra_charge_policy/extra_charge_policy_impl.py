from extra_charge_policy.extra_charge_policy_interface import BaseExtraCharge
from dto import User, Deer, Area
from const import OUTSIDE_CHARGE, FORBIDDEN_DISTRICT_CHARGE
from mock_db import find_deer_info, find_area_info, find_forbidden_area
from utils import calculate_distance
from dto import User


class OutsideDistrict(BaseExtraCharge):
    def calculate_extra_charge_amount(self, user: User):
        coords = (user.use_end_lat, user.use_end_lng)
        deer: Deer = find_deer_info(user.use_deer_name)
        area: Area = find_area_info(deer.deer_area_id)
        self.extra_charge_amount = calculate_distance(coords, area.area_boundary) * OUTSIDE_CHARGE
        return self.extra_charge_amount

    def calculate_after_extra_charge(self, user: User, before_fare: int):
        return before_fare - self.calculate_extra_charge_amount(self,user)


    def policy_check(self, user: User) -> bool:
        user_coods = (user.use_end_lng, user.use_end_lat)
        deer=find_deer_info(user.use_deer_name)
        area = find_area_info(deer.deer_area_id)
        if user_coods not in area.area_coords:
            return True
        return False


class AtForbiddenDistrict:
    def calculate_extra_charge_amount(self):
        return FORBIDDEN_DISTRICT_CHARGE

    def calculate_after_extra_charge(self, user: User, before_fare: int):
        return before_fare - self.calculate_extra_charge_amount(self, user)


    def policy_check(self, user: User) -> bool:
        user_coods = (user.use_end_lng, user.use_end_lat)
        forbidden = find_forbidden_area()
        if user_coods in forbidden.forbidden_area_coords:
            return True
        return False