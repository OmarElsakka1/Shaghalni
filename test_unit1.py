from website.helpers import Passwords, CheckEmail


def test_good_password():
    pw = Passwords('password123', 'password123')
    assert pw.is_good(display=False) == True

def test_bad_password():
    pw = Passwords('password123', 'password321')
    assert pw.is_good(display=False) == False

def test_short_password():
    pw = Passwords('123', '123')
    assert pw.is_good(display=False) == False


def test_valid_email():
    c = CheckEmail()
    assert c.is_in_form('test@example.com', False) == True

def test_invalid_email():
    c = CheckEmail()
    assert c.is_in_form('test@example', False) == False