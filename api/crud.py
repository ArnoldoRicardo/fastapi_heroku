from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from . import models, schemas


def get_products(db: Session, name: str):
    query = select(models.Product).where(
        models.Product.name.like(f'{name}%')
    )
    return db.execute(query).scalars().all()


def create_product(db: Session, product: schemas.ProductBase):
    db_product = models.Product(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_clients(db: Session, name: str):
    query = select(models.Client).where(
        or_(models.Client.name.like(f'{name}%'),
            models.Client.phone.like(f'%{name}%')
            ))
    return db.execute(query).scalars().all()


def create_client(db: Session, client: schemas.ClientBase):
    db_client = models.Client(name=client.name, phone=client.phone)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def create_note(db: Session, note: schemas.NoteBase):
    __import__('ipdb').set_trace()