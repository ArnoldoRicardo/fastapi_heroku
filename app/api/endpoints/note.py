from typing import List

from app import schemas
from app.api.deps import get_db
from app.crud import crudNote
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/', response_model=List[schemas.Note])
def get_notes(star_fecha: str, db: Session = Depends(get_db)):
    notes = crudNote.get_multi(db)
    if len(notes) < 1:
        raise HTTPException(status_code=404, detail="Items not found")
    return notes[0]


@router.post('/', response_model=schemas.Note)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    """create note

        actualizar que reciba el id del producto
    """
    new_nota = crudNote.create_note(db=db, note=note)
    return new_nota
