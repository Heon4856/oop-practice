from base_policy.base_policy_interface import BasePricing
import datetime

class BasePricingImpl(BasePricing):
    def calculate_fee(self, minute)-> int:
        minute = str(minute).split(":")[1]
        minute= int(minute)
        return self.basic_rate + minute*self.per_minute_rate

