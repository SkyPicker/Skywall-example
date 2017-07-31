from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql.functions import current_timestamp
from skywall.core.database import Model
from skywall.core.signals import Signal


before_example_create = Signal('before_example_create')
after_example_create = Signal('after_example_create')


class Example(Model):
    __tablename__ = 'example'

    id = Column(Integer, primary_key=True)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=current_timestamp())
    value = Column(String, nullable=False)

    def __repr__(self):
        return '<Example id={0.id}>'.format(self)
