# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_not_required
from tekton import router
from gaecookie.decorator import no_csrf
from pecas_app import pecas_facade
from routes.rests import new, edit, rest
from tekton.gae.middleware.redirect import RedirectResponse

@no_csrf
def index(_logged_user):
    contexto={ 'rest_new_path': router.to_path(rest.new),
                'rest_list_path': router.to_path(rest.index),
                'rest_delete_path': router.to_path(rest.delete),
                'rest_edit_path': router.to_path(rest.edit)
               }
    return TemplateResponse(contexto)

