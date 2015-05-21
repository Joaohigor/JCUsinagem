# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from pecas_app.pecas_model import PecasArco
from tekton.gae.middleware.json_middleware import JsonResponse
from pecas_app import pecas_facade

@no_csrf
def index():
    cmd = pecas_facade.list_pecas_cmd()
    peca_list = cmd()
    peca_form = pecas_facade.peca_form()
    peca_dcts = [peca_form.fill_with_model(m) for m in peca_list]
    return JsonResponse(peca_dcts)


def new(_logged_user,_resp, **peca_properties):
    cmd = pecas_facade.save_peca_cmd(**peca_properties)
    try:
        peca = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    peca_form = pecas_facade.peca_form()
    chave_de_usuario=_logged_user.key
    peca_arco=PecasArco(origin=chave_de_usuario,destination=peca.key)
    peca_arco.put()

    return JsonResponse(peca_form.fill_with_model(peca))



def edit(_resp, id, **peca_properties):
    cmd = pecas_facade.update_peca_cmd(id, **peca_properties)
    return _save_or_update_json_response(cmd, _resp)


def delete(_resp, id):
    cmd = pecas_facade.delete_peca_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)


def _save_or_update_json_response(cmd, _resp):
    try:
        peca = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    peca_form = pecas_facade.peca_form()
    return JsonResponse(peca_form.fill_with_model(peca))

