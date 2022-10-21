import pytest

from db.db_models import AppProspect


def test_prospectapp_pmodel():
    prospect_app = AppProspect(
        username="KT",
        email="test@gmail.com",
        appname="great app",
        appurl="com.greatapp.com",
        is_valid=True
    )

    assert prospect_app.username == 'KT'
    assert prospect_app.email == "test@gmail.com"
    assert prospect_app.appname == "great app"
    assert prospect_app.appurl == "com.greatapp.com"
    assert prospect_app.is_valid == True


# TODO Add off nominal tests
