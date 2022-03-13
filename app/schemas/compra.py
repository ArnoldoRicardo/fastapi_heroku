from pydantic import BaseModel

from .venta import VentaBase


class CompraBase(BaseModel):
    cantidad: float
    total: float
    factura: str


class Compra(VentaBase):
    id: int
    product_id: int

    class Config:
        orm_mode = True
