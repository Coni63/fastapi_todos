from typing import Optional
from pydantic import BaseModel, validator
import datetime
from enum import Enum
import re


class Status(Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    REMOVED = "REMOVED"


class TodoItem(BaseModel):
    id: int = -1
    title: str
    description: str
    created_at: Optional[datetime.datetime] = None
    status: Status = Status.TODO

    class Config:
        orm_mode = True
        from_orm = True
        use_enum_values = True

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

    def as_dict(self):
        ans = self.dict()
        if self.id == -1:
            del ans["id"]
        return ans
