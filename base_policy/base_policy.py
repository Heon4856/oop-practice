# 거리를 근거로 메기기.
class BasePricing:
    def __init__(self,name, basic_rate,per_minute_rate):
        self.name = name
        self.basic_rate = basic_rate
        self.per_minute_rate = per_minute_rate

    def calculate_fee(self, minute: int)-> int:
        return self.basic_rate + minute*self.per_minute_rate









