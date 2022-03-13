from datetime import date

from app.models import Note, Venta
from app.schemas.note import NoteCreate, NoteUpdate
from sqlalchemy.orm import Session

from .base import CRUDBase


class CrudNote(CRUDBase[Note, NoteCreate, NoteUpdate]):
    def create_note(self, db: Session, note: NoteCreate) -> Note:
        db_note = self.model(cliente=note.cliente,
                             total=note.total, anticipo=note.anticipo,
                             date=date.today())
        db.add(db_note)
        db.commit()
        db.refresh(db_note)
        for venta in note.ventas:
            db_venta = Venta(
                product_id=venta.product_id, cantidad=venta.cantidad,
                total=venta.total, note_id=db_note.id)
            db.add(db_venta)
            db.commit()
            db.refresh(db_venta)

        return db_note


crudNote = CrudNote(Note)
