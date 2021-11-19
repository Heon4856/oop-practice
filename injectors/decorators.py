import abc
import inspect
from functools import wraps
from policy_checker.policy_checker_impl import PolicyCheckerImplement
from policy_checker.policy_checker_interface import PolicyChecker


class Repo:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get(self):
        pass


class MySQLRepo(Repo):
    def get(self):
        print('MySQLRepo')


# providers = {
#     Repo: MySQLRepo
# }


def inject(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = inspect.getfullargspec(func).annotations
        for k, v in annotations.items():
            if v in providers:
                kwargs[k] = providers[v]

        return func(*args, **kwargs)

    return wrapper


class Usecase:
    @inject
    def __init__(self, abc: int, repo: Repo):
        self.age = abc
        self.repo = repo


providers = {
        PolicyChecker: PolicyCheckerImplement,
    }



# if __name__ == '__main__':
#     usecase = Usecase(11)
#     print(usecase)
#     print(usecase.age)
#     print(usecase.repo)
#     usecase.repo.get(usecase)
