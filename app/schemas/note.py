from datetime import date
from typing import List

from pydantic import BaseModel

from .venta import Venta, VentaCreate


class NoteBase(BaseModel):
    cliente: str
    total: float
    anticipo: float
    date: date


class NoteCreate(NoteBase):
    ventas: List[VentaCreate]


class NoteUpdate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    ventas: List[Venta] = []

    class Config:
        orm_mode = True
