import abc
from typing import List
from database_actions import DatabaseActions


class AbstractBankingProvider(abc.ABC):

    @abc.abstractmethod
    def log_in(self, user_id: str, user_pass: str) -> None:
        raise NotImplemented

    @abc.abstractmethod
    def check_if_logged(self) -> bool:
        raise NotImplemented

    @abc.abstractmethod
    def get_account_data(self, user_id: str) -> List:
        raise NotImplemented

    @abc.abstractmethod
    def transfer(self, user_login: str, amount_to_transfer: str, target_account: str) -> None:
        raise NotImplemented

    @abc.abstractmethod
    def log_out(self) -> str:
        raise NotImplemented


class MYSQLBankingProvider(AbstractBankingProvider):
    def __init__(self):
        self._logged_in = False
        self.database = DatabaseActions()

    def log_in(self, user_login: str, user_pass: str) -> None:
        data = self.database.get_login_and_password(user_login)
        try:
            if user_login == data[0] and user_pass == data[1]:
                print('Logged in')
                self._logged_in = True
            else:
                print('Dupa, złe dane logowania')
                self._logged_in = False
        except (IndexError, TypeError):
            print('Wrong login or password!')

    def check_if_logged(self) -> bool:
        return self._logged_in

    def get_account_data(self, user_login: str) -> List[tuple]:
        if self._logged_in:
            return self.database.get_account_data(user_login)
        else:
            print('User not logged in!')

    def transfer(self, user_login: str, amount_to_transfer: str, target_account: str) -> str:
        self.database.transfer_money(user_login, amount_to_transfer)
        return f'Transfered {amount_to_transfer} to account {target_account}'

    def log_out(self) -> None:
        self._logged_in = False


dupa = MYSQLBankingProvider()
dupa.log_in('1234', 'zxcv')
print(dupa.check_if_logged())
print(dupa.get_account_data('1234'))
print(dupa.transfer('1234', '5000', '123456789'))
print(dupa.get_account_data('1234'))
dupa.log_out()
print(dupa.check_if_logged())