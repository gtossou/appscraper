
from typing import Optional

from pydantic import BaseModel, EmailStr


class ProspectAppModel(BaseModel):
    """Class for parsing new stock data from a form."""
    user_name: str
    user_mail: EmailStr
    app_name: str
    app_url: str
    is_valid: Optional[bool] = False

    # @validator('stock_symbol')
    # def stock_symbol_check(cls, value):
    #     if not value.isalpha() or len(value) > 5:
    #         raise ValueError('Stock symbol must be 1-5 characters')
    #     return value.upper()
