from abc import ABC, abstractmethod
from dto import User
from exception_policy import BaseException

class QuickReturnPolicy(BaseException):

    def exception_change_amount(self,user: User,before_fare):
        return before_fare


    def calculate_exception(self, before_fare):
        return before_fare- self.exception_change_amount()



