from src.model.configs.base import Base
from sqlalchemy import Column, Integer, String

class Inscritos(Base):
   __tablename__ = 'Inscritos'

   id = Column(Integer, primary_key=True, autoincrement=True)
   nome = Column(String(100), nullable=False)
   email = Column(String(100), nullable=False)
   link = Column(String(100), nullable=True)
   evento_id = Column(Integer, ForeignKey('eventos.id'))
