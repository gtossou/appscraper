"""
SQL MODEL for appstats
"""

from datetime import datetime
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from pydantic import EmailStr


class AppProspect(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = None
    email: EmailStr
    appname: str = None
    appurl: str
    is_valid: Optional[bool] = False


class AppInfo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    appurl: str
    title: str
    description: Optional[str] = None
    summary: Optional[str] = None
    last_update: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
    approved: Optional[bool] = True
    stats: List["AppStats"] = Relationship(back_populates="appinfo")


class AppStats(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    installs: str = Field(index=True)
    min_installs: int = 0
    real_installs: int = 0
    score: float = 0
    ratings: int = 0
    reviews: int = 0
    last_update: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
    app_id: Optional[int] = Field(default=None, foreign_key="appinfo.id")
    appinfo: Optional[AppInfo] = Relationship(back_populates="stats")
