from app.db.base_class import Base
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship


class Note(Base):
    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String)
    total = Column(Float)
    anticipo = Column(Float)
    date = Column(Date)

    ventas = relationship("Venta")


class Venta(Base):
    id = Column(Integer, primary_key=True, index=True)
    cantidad = Column(Float)
    total = Column(Float)
    note_id = Column(Integer, ForeignKey("note.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    product_obj = relationship("Product", viewonly=True)

    @hybrid_property
    def product(self):
        return self.product_obj.nombre


class Compra(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    cantidad = Column(Float)
    total = Column(Float)
    factura = Column(String)
    product_id = Column(Integer, ForeignKey("product.id"))


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    categoria = Column(String)
    precio = Column(Float)

    ventas = relationship("Venta")
    compras = relationship("Compra")
