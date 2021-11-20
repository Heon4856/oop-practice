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


class PolicyCheckerImplement(PolicyChecker):
    def base_policy(self, deer_area_id:int, base_pricing:BasePricing ):
        base_pricing.basic_rate = base_policy_const[deer_area_id]["basic_rate"]
        base_pricing.per_minute_rate = base_policy_const[deer_area_id]["per_minute_rate"]
        return base_pricing
