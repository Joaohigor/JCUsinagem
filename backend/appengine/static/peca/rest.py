# -*- coding: utf-8 -*-
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from pecas_app import pecas_facade

def index():
    cmd = pecas_facade.list_pecas_cmd()
    pecas_list = cmd()
    pecas_form=pecas_facade.pecas_form()
    pecas_dcts= [pecas_form.fill_with_model(m) for m in pecas_list]
    return JsonResponse(pecas_dcts)

def new(_resp, **pecas_propriedades):
    cmd = pecas_facade.save_pecas_cmd(**pecas_propriedades)
    return _save_or_update_json_response(cmd, _resp)

def edit(_resp, pecas_id, **pecas_propriedades):
    cmd = pecas_facade.update_pecas_cmd(pecas_id, **pecas_propriedades)
    return _save_or_update_json_response(cmd, _resp)

def delete(pecas_id):
    pecas_facade.delete_pecas_cmd(pecas_id)()

def _save_or_update_json_response(cmd, _resp):
    try:
        pecas = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.erros)
    pecas_form=pecas_facade.pecas_form()
    return JsonResponse(pecas_form.fill_with_model(pecas))