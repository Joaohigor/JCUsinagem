# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from pecas_app.pecas_model import Peca
from routes.rests.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Peca.query().get())
        redirect_response = save(titulo='titulo_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_peca = Peca.query().get()
        self.assertIsNotNone(saved_peca)
        self.assertEquals('titulo_string', saved_peca.titulo)

    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set(['titulo']), set(errors.keys()))
        self.assert_can_render(template_response)
