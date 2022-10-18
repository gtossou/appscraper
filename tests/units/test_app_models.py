import pytest

from ...web.models import ProspectAppModel


def test_prospectapp_pmodel():
    prospect_app = ProspectAppModel(
        user_name="KT",
        user_mail="test@gmail.com",
        app_name="great app",
        app_url="com.greatapp.com",
        is_valid=True
    )

    assert prospect_app.user_name == 'KT'
    assert prospect_app.user_mail == "test@gmail.com"
    assert prospect_app.app_name == "great app"
    assert prospect_app.app_url == "com.greatapp.com"
    assert prospect_app.is_valid == True


# TODO Add off nominal tests
