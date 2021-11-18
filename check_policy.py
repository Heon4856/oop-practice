class CheckPolicy:
    def __init__(self, deer_id):
        self.base_policy = BasePolicy(deer_id)
        self.discount_policy = DiscountPolicy(deer_id)
        self.cost_policy = discount_policy(deer_id)
        self.exception_policy = ExceptionPolicy(deer_id)