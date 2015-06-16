# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, UpdateCommand
from gaegraph.business_base import NodeSearch, DeleteNode, DestinationsSearch, CreateArc, DeleteArcs
from pecas_app.pecas_commands import ListPecaCommand, SavePecaCommand, UpdatePecaCommand, PecaForm,\
    GetPecaCommand, DeletePecaCommand
from pecas_app.pecas_model import PecasArco


def save_peca_cmd(**peca_properties):
    """
    Command to save Peca entity
    :param peca_properties: a dict of properties to save on model
    :return: a Command that save Peca, validating and localizing properties received as strings
    """
    return SavePecaCommand(**peca_properties)


def update_peca_cmd(peca_id, **peca_properties):
    """
    Command to update Peca entity with id equals 'peca_id'
    :param peca_properties: a dict of properties to update model
    :return: a Command that update Peca, validating and localizing properties received as strings
    """
    return UpdatePecaCommand(peca_id, **peca_properties)


def list_pecas_cmd(peca):
    """
    Command to list Peca entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListPecaCommand()


def peca_form(**kwargs):
    """
    Function to get Peca's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return PecaForm(**kwargs)


def get_peca_cmd(peca_id):
    """
    Find peca by her id
    :param peca_id: the peca id
    :return: Command
    """
    return GetPecaCommand(peca_id)



def delete_peca_cmd(peca_id):
    """
    Construct a command to delete a Peca
    :param peca_id: peca's id
    :return: Command
    """
    return DeletePecaCommand(peca_id)
