"""
SQL MODEL for Appinfo
"""

from sqlmodel import Field, SQLModel


class AppInfo(SQLModel, table=True):
    id: str = Field(primary_key=True)
    title: str = Field(default=None)
    description: str = Field(default=None)
    summary: str = Field(default=None)
