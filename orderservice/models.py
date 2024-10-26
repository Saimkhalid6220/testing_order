from datetime import datetime
from enum import Enum
from sqlmodel import Field, SQLModel


class OrderStatus(str,Enum):
    PENDING = "pending"
    RECEIVED = "received"
    CANCELED = "canceled"

class BaseOrder(SQLModel,table=True):
    order_id:int=Field(default=None,primary_key=True)
    placed_by:str=Field()
    product_name:str=Field()
    shop_name:str=Field()
    adress:str=Field()
    product_price:float=Field()
    quantity:int=Field()
    status:OrderStatus=Field(default=OrderStatus.PENDING)
    created_at:datetime=Field(default_factory=datetime)

    