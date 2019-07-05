import abc
from typing import List


class AbstractBankingProvider(abc.ABC):

    @abc.abstractmethod
    def log_in(self, user_id: int, user_pass: str) -> None:
        raise NotImplemented

    @abc.abstractmethod
    def check_if_logged(self, user_id: int) -> bool:
        raise NotImplemented

    @abc.abstractmethod
    def get_account_data(self, user_id: int) -> List:
        raise NotImplemented

    @abc.abstractmethod
    def transfer(self, user_id: int, amount_to_transfer: float, target_account: int) -> None:
        raise NotImplemented

    @abc.abstractmethod
    def log_out(self, user_id: int) -> None:
        raise NotImplemented


class SQLiteBankingProvider(AbstractBankingProvider):
    def __init__(self):
        self._logged_in = False
        # self._name = ''
        # self._surname = ''
        # self._account_number = 0
        # self._balance = 0
        # self._login = ''
        # self._password = ''
        # self._address = ''
        # self._pesel = 0

    def log_in(self, user_id: int, user_pass: str) -> None:
        pass

    def check_if_logged(self, user_id: int) -> bool:
        return self._logged_in

    def get_account_data(self, user_id: int) -> List:
        pass

    def transfer(self, user_id: int, amount_to_transfer: float, target_account: int) -> None:
        pass

    def log_out(self, user_id: int) -> None:
        pass


x = SQLiteBankingProvider('dupa')