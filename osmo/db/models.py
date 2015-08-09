# -*- coding: utf-8 -*-
#
# Refrence Openstack oslo.db
# File: oslo.db/oslo.db/sqlalchemy/models.py
#


from datetime import datetime

from oslo_db.sqlalchemy import models
from sqlalchemy.ext import declarative
from sqlalchemy import Column, Integer
from sqlalchemy import DateTime

from osmo.core.timeutils import utcnow


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
    id = Column(Integer, primary_key=True)


class TimestampMixin(object):
    """oslo.db - TimestampMixin
    """
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, onupdate=utcnow)

ModelBase = models.ModelBase
