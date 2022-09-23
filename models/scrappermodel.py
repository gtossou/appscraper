"""
SQL MODEL for appstats
"""

from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class AppInfo(SQLModel, table=True):
    id: str = Field(primary_key=True)
    title: str = Field(default=None)
    description: str = Field(default=None)
    summary: str = Field(default=None)
    stats: List["AppStats"] = Relationship(back_populates="appinfo")


class AppStats(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    installs: str = Field(index=True)
    min_installs: int = Field(default=0)
    real_installs: int = Field(default=0)
    score: float = Field(default=0)
    ratings: int = Field(default=0)
    reviews: int = Field(default=0)
    insert_time: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
    app_id: Optional[int] = Field(default=None, foreign_key="appinfo.id")
    info: Optional[AppInfo] = Relationship(back_populates="appstats")
