"""
SQL MODEL for appstats
"""

from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class AppStats(SQLModel, table=True):
    installs: str = Field(index=True)
    min_installs: int = Field(default=0)
    real_installs: int = Field(default=0)
    score: float = Field(default=0)
    ratings: int = Field(default=0)
    reviews: int = Field(default=0)
    insert_time: datetime = Field(
        default_factory=datetime.utcnow, nullable=False, primary_key=True)
    app_id: str = Field(
        default=None, primary_key=True)
