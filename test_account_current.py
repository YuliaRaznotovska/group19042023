def test_original_balance(new_current_account):
    assert new_current_account.balance == 0


def test_is_credit_allowed(new_current_account):
    assert new_current_account.credit_allowed is True


def test_withdraw_money(new_current_account):
    new_current_account.balance = 50
    new_current_account.withdraw_money(30)
    assert new_current_account.balance == 20


def test_withdraw_money_over_limit(new_current_account):
    new_current_account.balance = 100
    new_current_account.withdraw_money(150)
    assert AssertionError


def test_change_credit_status(new_current_account):
    new_current_account.change_credit_status(False)
    assert new_current_account.credit_allowed is False


def test_deposit_money_int(new_current_account):
    new_current_account.deposit_money(65)
    assert new_current_account.balance == 65


def test_deposit_money_float(new_current_account):
    new_current_account.deposit_money(15.8)
    assert new_current_account.balance == 15.8
