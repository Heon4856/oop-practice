from exception_policy_interface import BaseException

class QuickReturnPolicy(BaseException):

    def exception_change_amount(self,before_fare: int):
        return before_fare


    def calculate_exception(self, before_fare: int ):
        return before_fare- self.exception_change_amount()



