from const import EXCEIPTION_TIMEDELTA
from exception_policy.exception_policy_interface import BaseException
from dto import User

class QuickReturnException(BaseException):

    def calculate_exception_change_amount(self,user:User, before_fare: int):
        return before_fare


    def calculate_exception(self, user:User, before_fare: int ):
        return before_fare- self.exception_change_amount(self,user, before_fare)

    def policy_check(self, user: User) -> bool:
        if user.use_end_at - user.use_start_at < EXCEIPTION_TIMEDELTA:
            return True
        return False
