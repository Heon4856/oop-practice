from policy_checker.policy_checker_interface import PolicyChecker
from const import base_policy_const
from dto import User
from utils import calculate_distance
from discount_policy.discount_policy_impl import ParkingZoneDiscount, EarlyReuseDiscount
from extra_charge_policy.extra_charge_policy_impl import OutsideDistrict, AtForbiddenDistrict
from exception_policy.exception_policy_impl import QuickReturnPolicy
from mock_db import find_parking_zone, find_user_last_use, find_area_info, find_forbidden_area
from const import REUSE_TIMEDELTA, EXCEIPTION_TIMEDELTA
from base_policy.base_policy_interface import BasePricing
from injectors.providers import inject2


class PolicyCheckerImplement(PolicyChecker):

    @inject2
    def base_policy(self, deer_area_id:int, base_pricing:BasePricing ):
        base_pricing.basic_rate = base_policy_const[deer_area_id]["basic_rate"]
        base_pricing.per_minute_rate = base_policy_const[deer_area_id]["per_minute_rate"]
        return base_pricing

    def discount_policy(self, deer_area_id, user: User):
        discount_policies = []
        parkingzone = find_parking_zone()
        user_coods = (user.use_end_lng, user.use_end_lat)
        parkingzone_coods = (parkingzone.parkingzone_center_lng, parkingzone.parkingzone_center_lat)
        if parkingzone.parkingzone_radius < calculate_distance(user_coods, parkingzone_coods):
            parkingzone_policy = ParkingZoneDiscount()
            parkingzone_policy.basic_rate = base_policy_const[deer_area_id]["basic_rate"]
            parkingzone_policy.per_minute_rate = base_policy_const[deer_area_id]["per_minute_rate"]
            discount_policies.append(parkingzone_policy)

        if user.use_start_at - find_user_last_use() < REUSE_TIMEDELTA:
            early_reuse_policy = EarlyReuseDiscount()
            early_reuse_policy.basic_rate = base_policy_const[deer_area_id]["basic_rate"]
            early_reuse_policy.per_minute_rate = base_policy_const[deer_area_id]["per_minute_rate"]
            discount_policies.append(early_reuse_policy)

        return discount_policies

    def extra_charge_policy(self, deer_area_id, user: User):
        extra_charge_policies = []
        user_coods = (user.use_end_lng, user.use_end_lat)
        area = find_area_info(deer_area_id)
        if user_coods not in area.area_coords:
            extra_charge_policies.append(OutsideDistrict)

        forbidden = find_forbidden_area()
        if user_coods in forbidden.forbidden_area_coords:
            extra_charge_policies.append(AtForbiddenDistrict)

        return extra_charge_policies

    def exception_policy(self, user):
        if user.use_end_at - user.use_start_at < EXCEIPTION_TIMEDELTA:
            return QuickReturnPolicy

    def check_policy(self, user, deer_area_id):
        self.base_policy = self.base_policy(deer_area_id)
        self.discount_policy = self.discount_policy(deer_area_id, user)
        self.extra_charge_policy = self.extra_charge_policy(deer_area_id, user)
        self.exception_policy = self.exception_policy(user)
