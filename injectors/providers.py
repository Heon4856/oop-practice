import inspect
from functools import wraps

from base_policy.base_policy_interface import BasePricing
from base_policy.base_policy_impl import BasePricingImpl

providers = {
        BasePricing : BasePricingImpl,
    }



def inject2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = inspect.getfullargspec(func).annotations
        for k, v in annotations.items():
            if v in providers:
                kwargs[k] = providers[v]
        return func(*args, **kwargs)

    return wrapper