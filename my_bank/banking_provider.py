import abc
from typing import List
from my_bank.database_actions import CreateDatabase


class AbstractBankingProvider(abc.ABC):

    @abc.abstractmethod
    def log_in(self, user_id: str, user_pass: str) -> None:
        raise NotImplemented

    @abc.abstractmethod
    def check_if_logged(self, user_id: str) -> bool:
        raise NotImplemented

    @abc.abstractmethod
    def get_account_data(self, user_id: str) -> List:
        raise NotImplemented

    @abc.abstractmethod
    def transfer(self, user_id: str, amount_to_transfer: str, target_account: str) -> None:
        raise NotImplemented

    @abc.abstractmethod
    def log_out(self, user_id: str) -> None:
        raise NotImplemented


class SQLiteBankingProvider(AbstractBankingProvider):
    def __init__(self):
        self._logged_in = False
        self.database = CreateDatabase('resources/database.db')

    def log_in(self, user_login: str, user_pass: str) -> None:
        data = self.database.get_login_and_password(user_login)
        try:
            if user_login == data[0][0] and user_pass == data[0][1]:
                print('Logged in')
                self._logged_in = True
            else:
                print('Dupa, złe dane logowania')
                self._logged_in = False
        except IndexError:
            print('Wrong login or password!')

    def check_if_logged(self, user_id: str) -> bool:
        return self._logged_in

    def get_account_data(self, user_login: str) -> List[tuple]:
        if self._logged_in:
            return self.database.get_account_data(user_login)
        else:
            print('User not logged in!')

    def transfer(self, user_id: str, amount_to_transfer: str, target_account: str) -> None:
        pass

    def log_out(self, user_id: str) -> None:
        pass


dupa = SQLiteBankingProvider()
dupa.log_in('1234', 'zxcv')
print(dupa.get_account_data('1234'))
