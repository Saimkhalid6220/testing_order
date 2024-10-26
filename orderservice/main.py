from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session, select

from orderservice.db import get_session, lifespan
from orderservice.models import BaseOrder, OrderStatus

app = FastAPI(lifespan=lifespan)

@app.post('/order',response_model=BaseOrder)
def create_order(db:Annotated[Session,Depends(get_session)],order:BaseOrder)->BaseOrder:
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

@app.patch('/order/{id}',response_model=BaseOrder)
def update_order_status(db:Annotated[Session,Depends(get_session)],id:int,status:OrderStatus)->BaseOrder:
    order = db.exec(select(BaseOrder).filter(BaseOrder.order_id==id)).one_or_none()
    if not order:
        raise HTTPException(status_code=404,detail="order not found")
    order.status = status
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

@app.get('/order/{id}',response_model=BaseOrder)
def get_order_by_id(db:Annotated[Session,Depends(get_session)],id:int)->BaseOrder:
    order = db.exec(select(BaseOrder).filter(BaseOrder.order_id==id)).one()
    if not order:
        raise HTTPException(status_code=404,detail="order not found")
    return order
    



