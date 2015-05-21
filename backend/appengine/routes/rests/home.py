# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from pecas_app import pecas_facade
from routes.rests import new, edit, rest
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    context = {'rest_list_path': router.to_path(rest.index),
               'rest_new_path': router.to_path(rest.new)}
    return TemplateResponse(context, 'rests/rest_home.html')


def delete(peca_id):
    pecas_facade.delete_peca_cmd(peca_id)()
    return RedirectResponse(router.to_path(index))

