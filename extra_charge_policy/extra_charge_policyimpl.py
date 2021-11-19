from extra_charge_policy_interface import BaseExtraCharge
from dto import User, Deer, Area
from const import OUTSIDE_CHARGE, FORBIDDEN_DISTRICT_CHARGE
from mock_db import find_deer_info, find_area_info
from utils import calculate_distance


class OutsideDistrict(BaseExtraCharge):
    def extra_charge_amount(self ):
        coords = (self.user.use_end_lat, self.user.use_end_lng)
        deer: Deer = find_deer_info(self.user.use_deer_name)
        area: Area = find_area_info(deer.deer_area_id)
        return calculate_distance(coords, area.area_bounday) * OUTSIDE_CHARGE

    def calculate_after_extra_charge(self, before_fare):
        return before_fare - self.extra_charge_amount


class AtForbiddenDistrict:
    def extra_charge_amount(self):
        return FORBIDDEN_DISTRICT_CHARGE

    def calculate_after_extra_charge(self, before_fare):
        return before_fare - self.extra_charge_amount


