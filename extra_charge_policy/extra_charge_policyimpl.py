from extra_charge_policy import BaseExtraCharge
from dto import User, Deer, Area
from const import OUTSIDE_CHARGE, FORBIDDEN_DISTRICT_CHARGE


class outside_strict(BaseExtraCharge):
    def extra_charge_amount(self, user: User):
        coords = (User.use_end_lat, User.use_end_lng)
        deer: Deer = find(User.use_deer_name)
        area: Area = find_area(deer.deer_area_id)

        return far_away(coords, area.area_bounday) * OUT_SIDE_CHARGE

    def calculate_after_extra_charge(self, before_fare):
        return before_fare - self.extra_charge_amount


class at_not_district:
    def extra_charge_amount(self, user: User):
        return FORBIDDEN_DISTRICT_CHARGE

    def calculate_after_extra_charge(self, before_fare):
        return before_fare - self.extra_charge_amount
