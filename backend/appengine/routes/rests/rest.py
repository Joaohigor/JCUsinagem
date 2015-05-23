# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext.ndb.key import Key
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from pecas_app.pecas_model import PecasArco
from tekton.gae.middleware.json_middleware import JsonResponse
from pecas_app import pecas_facade
from tekton import router

@no_csrf
def index():
    cmd = pecas_facade.list_pecas_cmd()
    peca_list = cmd()
    peca_form = pecas_facade.peca_form()
    peca_dcts = [peca_form.fill_with_model(m) for m in peca_list]
    print(peca_dcts)
    return JsonResponse(peca_dcts)


def new(_logged_user,_resp, **peca_properties):
    cmd = pecas_facade.save_peca_cmd(**peca_properties)
    try:
        peca = cmd()
        chave_de_usuario=_logged_user.key
        peca_arco=PecasArco(origin=chave_de_usuario,destination=peca.key)
        peca_arco.put()

    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)


    return _save_or_update_json_response(peca)



def edit(_resp,id, **peca_properties):
    cmd = pecas_facade.update_peca_cmd(id, **peca_properties)
    try:
        peca = cmd()


    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    return _save_or_update_json_response(cmd)


def delete(_resp, id):
    # # cmd = pecas_facade.delete_peca_cmd(id)
    # key = Key('Peca', int(id))
    # key.get()
    # try:
    #     # cmd()
    #     key.delete()
    #     arco = PecasArco.query(PecasArco.destination == key.key).fetch()
    #     arco[0].key.delete()
    # except Exception as e:
    #     _resp.status_code = 400
    #     return JsonResponse({})
    # form = pecas_facade.peca_form()
    # return JsonResponse(form.fill_with_model(key))
    return JsonResponse({})


def _save_or_update_json_response(cmd):
    peca_form = pecas_facade.peca_form()
    return JsonResponse(peca_form.fill_with_model(cmd))

