import pytest
from lib.login import check_login_credentials
from core.utils import load_test_data_from_csv


login_test_data, columns = load_test_data_from_csv("login.csv")



@pytest.mark.parametrize(",".join(columns), login_test_data)
def test_login(username, password, expected_result):
    actual_result = check_login_credentials(username=username, password=password)
    assert actual_result == expected_result