"""
SQL MODEL
"""

from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class appInfo(SQLModel, table=True):
    id: str = Field(primary_key=True)
    title: str = Field(default=None)
    description: str = Field(default=None)
    summary: str = Field(default=None)


class appStats(SQLModel, table=True):
    installs: str = Field(index=True)
    min_installs: int = Field(default=0)
    real_installs: int = Field(default=0)
    score: float = Field(default=0)
    ratings: int = Field(default=0)
    reviews: int = Field(default=0)
    insert_time: datetime.datetime = Field(
        default_factory=datetime.utcnow, nullable=False, primary_key=True)
    app_id: Optional[int] = Field(
        default=None, foreign_key="appInfo.id", primary_key=True)
