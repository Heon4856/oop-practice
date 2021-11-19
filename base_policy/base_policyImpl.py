from base_policy_interface import BasePricing

class BasePricingImpl(BasePricing):
    def calculate_fee(self, minute: int)-> int:
        return self.basic_rate + minute*self.per_minute_rate


