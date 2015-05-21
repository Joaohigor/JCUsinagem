# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from pecas_app.pecas_model import Peca



class PecaSaveForm(ModelForm):
    """
    Form used to save and update Peca
    """
    _model_class = Peca
    _include = [Peca.title,Peca.price,Peca.amount,Peca.creation]

class PecaFormTable(ModelForm):
    _model_class = Peca
    _include = [Peca.title,Peca.price,Peca.amount,Peca.creation]


class PecaForm(ModelForm):
    _model_class = Peca
    _include = [Peca.title,Peca.price,Peca.amount]

class GetPecaCommand(NodeSearch):
    _model_class = Peca


class DeletePecaCommand(DeleteNode):
    _model_class = Peca


class SavePecaCommand(SaveCommand):
    _model_form_class = PecaSaveForm


class UpdatePecaCommand(UpdateNode):
    _model_form_class = PecaSaveForm


class ListPecaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListPecaCommand, self).__init__(Peca.query_by_creation())

