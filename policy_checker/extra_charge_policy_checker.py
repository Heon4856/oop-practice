from dto import User
from policy_checker.policy_checker_interface import PolicyChecker


class ExtraPolicyCheckerImplement(PolicyChecker):
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