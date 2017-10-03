from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime,Float

from ..database import db
from ..mixins import CRUDModel

class LetadloSQL(CRUDModel):
    __tablename__ = 'letadlo'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    pohlavi = Column(Integer, nullable=True, index=False)#1=hovezi,2=vepr,3=kure
    typ_letadla = Column(Integer, nullable=True, index=False)#1=predni,2=zadni

    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
