from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    disable: bool


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
