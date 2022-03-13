from pydantic import BaseModel


class VentaBase(BaseModel):
    cantidad: float
    total: float


class Venta(VentaBase):
    id: int
    note_id: int
    _product_id: int
    product: str

    class Config:
        orm_mode = True


class VentaCreate(VentaBase):
    product_id: int
