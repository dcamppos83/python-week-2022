#from dataclasses import dataclass ## já acompanha o python, não precisa instalar
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select

#@dataclass
# class Beer():
#     name: str
#     style: str
#     flavor: int
#     image: int
#     cost: int

class Beer(SQLModel, table=True): #herança. Com isso ganhamos um ORM
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int

brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=8, cost=8)