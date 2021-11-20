from discount_policy.discount_policy_interface import BaseDiscount
from dto import User
from injectors.decorators import inject
from policy_checker.policy_checker_interface import PolicyChecker


class DiscountPolicyCheckerImplement(PolicyChecker):
    @inject
    def __init__(self, baseDiscount : BaseDiscount):
        self.discount_policy = baseDiscount

    def discount_policy(self, deer_area_id, user: User):
        discount_policies = []

        return discount_policies