# -*- coding: utf-8 -*-


from datetime import datetime
from oslo.db.sqlalchemy import models
from sqlalchemy.ext import declarative
import sqlalchemy as sa


from timeutils import utcnow


class TableNameMixin(object):

    @declarative.declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'


class JSONSeriableMixin(object):

    def __iter__(self):
        """ Returns a JSON representation of an SQLAlchemy-backed object.
        """

        for col in self._sa_class_manager.mapper.mapped_table.columns:
            value = getattr(self, col.name)
            if isinstance(value, datetime):
                value = datetime.strftime(value, '%F %T')
            yield (col.name, value)


class HasIdMixin(object):
    id = sa.Column(sa.Integer, primary_key=True)


class TimestampMixin(object):
    created_at = sa.Column(sa.DateTime, default=utcnow)
    updated_at = sa.Column(sa.DateTime, onupdate=utcnow)

ModelBase = models.ModelBase
