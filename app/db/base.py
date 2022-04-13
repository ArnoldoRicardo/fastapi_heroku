# Note: we need import here the other models to be correctle maped for alembic
from app.db.base_class import Base  # nq
from app.models import User  # nq
from app.models import Compra, Note, Product, Venta  # nq
