from const import KUNKOOK_PRICE,KUNKOOK_NAME,KUNKOOK_EXTRA_CHARGE

class BasePricing:
    def __init__(self,name, base_price, extra_minute_price):
        self.name = name
        self.base_price = base_price
        self.extra_minute_price = extra_minute_price

    def __str__(self):
        return str({"name" : f'{self.name}',
                "base": f'{self.base_price}',
                "extra": f'{self.extra_minute_price}'})




kunkook = BasePricing(KUNKOOK_NAME, KUNKOOK_PRICE, KUNKOOK_EXTRA_CHARGE)





