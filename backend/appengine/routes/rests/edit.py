# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from pecas_app import pecas_facade
from routes import rests
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(peca_id):
    peca = pecas_facade.get_peca_cmd(peca_id)()
    peca_form = pecas_facade.peca_form()
    context = {'save_path': router.to_path(save, peca_id), 'peca': peca_form.fill_with_model(peca)}
    return TemplateResponse(context, 'rests/rest_form.html')


def save(peca_id, **peca_properties):
    cmd = pecas_facade.update_peca_cmd(peca_id, **peca_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors, 'peca': peca_properties}

        return TemplateResponse(context, 'rests/rest_form.html')
    return RedirectResponse(router.to_path(rests))

