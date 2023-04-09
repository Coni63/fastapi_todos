from pydantic import BaseModel, validator
from abc import ABC
import datetime
from enum import Enum
import re


class Status(Enum):
    TODO = 0
    IN_PROGRESS = 1
    DONE = 2
    REMOVED = 3


class IItem(BaseModel, ABC):
    id: int
    title: str
    description: str
    created_at: datetime.datetime
    status: Status = Status.TODO

    @validator('title')
    def title_match_regex(cls, value):
        pattern = "[A-Za-z0-9_ ]{1,100}"
        if re.match(pattern, value):
            return value

        raise ValueError(f"Invalid title: must match the regex `{pattern}`")

    @validator('description')
    def max_length(cls, value):
        if len(value) < 1000:
            return value

        raise ValueError("Description is too long (max 1000 chars)")
