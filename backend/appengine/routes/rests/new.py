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
def index():
    return TemplateResponse({'save_path': router.to_path(save)}, 'rests/rest_form.html')


def save(**peca_properties):
    cmd = pecas_facade.save_peca_cmd(**peca_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'peca': peca_properties}

        return TemplateResponse(context, 'rests/rest_form.html')
    return RedirectResponse(router.to_path(rests))

