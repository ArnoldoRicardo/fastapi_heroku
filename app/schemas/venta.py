from pydantic import BaseModel


class VentaBase(BaseModel):
    cantidad: float
    total: float


class Venta(VentaBase):
    id: int
    note_id: int
    product_id: int

    class Config:
        orm_mode = True


class VentaCreate(VentaBase):
    product_id: int
