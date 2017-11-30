# -*- coding: utf-8 -*-
from sqlalchemy import desc

from .database import db_session


class Service(object):
    __model__ = None


    def _isinstance(self, model, raise_error=True):
        rv = isinstance(model, self.__model__)
        if not rv and raise_error:
            raise ValueError('%s is not of type %s' % (model, self.__model__))
        return rv


    def _preprocess_params(self, kwargs):
        kwargs.pop('csrf_token', None)
        return kwargs


    def save(self, model):
        self._isinstance(model)
        db_session.add(model)
        db_session.commit()
        return model


    def store(self, model):
        self._isinstance(model)
        db_session.add(model)
        return model


    def all(self):
        return self.__model__.query.all()


    def get(self, id):
        return self.__model__.query.get(id)


    def get_all(self, *ids):
        return self.__model__.query.filter(self.__model__.id.in_(ids)).all()


    def find(self, **kwargs):
        return self.__model__.query.filter_by(**kwargs)


    def count(self, **kwargs):
        return self.find(**kwargs).count()


    def first_or_404(self, **kwargs):
        rv = self.find(**kwargs).first()
        if rv is None:
            abort(404)
        return rv


    def first(self, **kwargs):
        return self.find(**kwargs).first()


    def get_or_404(self, id):
        return self.__model__.query.get_or_404(id)


    def new(self, **kwargs):
        return self.__model__(**self._preprocess_params(kwargs))


    def create(self, **kwargs):
        return self.save(self.new(**kwargs))


    def update(self, model, **kwargs):
        self._isinstance(model)
        for k, v in self._preprocess_params(kwargs).items():
            setattr(model, k, v)
        self.save(model)
        return model


    def delete(self, model):
        self._isinstance(model)
        db_session.delete(model)
        db_session.commit()


    def latest(self, limit=1, **kwargs):
        return self.__model__.query.filter_by(**kwargs).order_by(desc(self.__model__.id)).limit(limit).all()


    def serialize(self, model):
        return model.serialize
