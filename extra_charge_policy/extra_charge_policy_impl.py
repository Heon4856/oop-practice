from extra_charge_policy.extra_charge_policy_interface import BaseExtraCharge
from dto import User, Deer, Area
from const import OUTSIDE_CHARGE, FORBIDDEN_DISTRICT_CHARGE
from mock_db import find_deer_info, find_area_info
from utils import calculate_distance


class OutsideDistrict(BaseExtraCharge):
    def calculate_extra_charge_amount(self ,user: User):
        coords = (user.use_end_lat, user.use_end_lng)
        deer: Deer = find_deer_info(user.use_deer_name)
        area: Area = find_area_info(deer.deer_area_id)
        self.extra_charge_amount =  calculate_distance(coords, area.area_bounday) * OUTSIDE_CHARGE
        return self.extra_charge_amount

    def calculate_after_extra_charge(self, before_fare: int ):
        return before_fare - self.extra_charge_amount


class AtForbiddenDistrict:
    def extra_charge_amount(self):
        return FORBIDDEN_DISTRICT_CHARGE

    def calculate_after_extra_charge(self, before_fare: int):
        return before_fare - self.extra_charge_amount


