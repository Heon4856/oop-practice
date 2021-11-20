from dto import User
from policy_checker.policy_checker_interface import PolicyChecker


class ExeptionPolicyCheckerImplement(PolicyChecker):
    def exception_policy(self, user):
        if user.use_end_at - user.use_start_at < EXCEIPTION_TIMEDELTA:
            return QuickReturnPolicy