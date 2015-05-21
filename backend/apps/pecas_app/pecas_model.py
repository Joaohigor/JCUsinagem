# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node, Arc
from gaeforms.ndb import property


class Peca(Node):
    title = ndb.StringProperty(required=True)
    price = ndb.FloatProperty(required=True)
    amount = ndb.IntegerProperty(required=True)

class PecasArco(Arc):
    origin = ndb.KeyProperty(required=True)
    destination = ndb.KeyProperty(Peca,required=True)

