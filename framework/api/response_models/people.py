from typing import List, Optional

from pydantic import BaseModel, HttpUrl

from framework.api.response_models.person import PersonResponse


class PeopleResponse(BaseModel):
    count: int
    next: Optional[HttpUrl] = None
    previous: Optional[HttpUrl] = None
    results: List[PersonResponse]
