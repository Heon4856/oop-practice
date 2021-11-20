from discount_policy.discount_policy_interface import BaseDiscount
from policy_checker.policy_checker_interface import PolicyChecker
from typing import List
from dto import User

class DiscountPolicyCheckerImplement(PolicyChecker):
    def __init__(self, base_discounts: List[BaseDiscount]):
        self.discount_policies = base_discounts


    def policy_check(self, user:User):
        discount_policy_for_user = []
        for policy in self.discount_policies:
            if policy.policy_check(policy, user):
                discount_policy_for_user.append(policy)

        print( self.discount_policies)
        return discount_policy_for_user