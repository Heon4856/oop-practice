#TODO
# parking zone 30%
# 30min limit

#여러개가 한꺼번에 적용될 수있음.
from const import KUNKOOK_PRICE,KUNKOOK_NAME,KUNKOOK_EXTRA_CHARGE
from abc import ABC, abstractmethod
from

class BaseDiscount(ABC):

    active: bool

    @abstractmethod
    def calculate_discount(self):
        pass



class ParkingZone(BaseDiscount):

    discount_rate = 0.3

    def calculate_discount(self):


class second_use:
    base_cost = 0
