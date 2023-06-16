import pytest


def test_original_balance(new_deposit_account):
    assert new_deposit_account.balance == 0


def test_is_credit_allowed(new_deposit_account):
    assert new_deposit_account.credit_allowed is False


def test_withdraw_money(new_deposit_account):
    new_deposit_account.balance = 100
    new_deposit_account.withdraw_money(30)
    assert new_deposit_account.balance == 70


def test_withdraw_money_over_limit(new_deposit_account):
    new_deposit_account.balance = 100
    with pytest.raises(ValueError):
        new_deposit_account.withdraw_money(850)


def test_change_credit_status(new_deposit_account):
    new_deposit_account.change_credit_status(True)
    assert new_deposit_account.credit_allowed is True


def test_deposit_money_int(new_deposit_account):
    new_deposit_account.deposit_money(98)
    assert new_deposit_account.balance == 98


def test_deposit_money_float(new_deposit_account):
    new_deposit_account.deposit_money(23.3)
    assert new_deposit_account.balance == 23.3
