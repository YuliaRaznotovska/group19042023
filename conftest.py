import pytest

from models import Account, AccountType


@pytest.fixture()
def new_current_account():
    account_type = AccountType.CURRENT
    account = Account(account_type=account_type)
    yield account
    del account


@pytest.fixture()
def new_deposit_account():
    account_type = AccountType.DEPOSIT
    account = Account(account_type=account_type)
    yield account
    del account
