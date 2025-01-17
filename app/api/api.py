from app.api.deps import oauth2_scheme
from app.api.endpoints import note, product
from fastapi import APIRouter, Depends

api_router = APIRouter()


@api_router.get('/')
def main(token: str = Depends(oauth2_scheme)):
    return {"info": "hola soy una api"}


api_router.include_router(note.router, prefix='/note', tags=["note"])
api_router.include_router(product.router, prefix='/product', tags=["product"])
