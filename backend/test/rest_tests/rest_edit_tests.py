# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from pecas_app.pecas_model import Peca
from routes.rests.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        peca = mommy.save_one(Peca)
        template_response = index(peca.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        peca = mommy.save_one(Peca)
        old_properties = peca.to_dict()
        redirect_response = save(peca.key.id(), titulo='titulo_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_peca = peca.key.get()
        self.assertEquals('titulo_string', edited_peca.titulo)
        self.assertNotEqual(old_properties, edited_peca.to_dict())

    def test_error(self):
        peca = mommy.save_one(Peca)
        old_properties = peca.to_dict()
        template_response = save(peca.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set(['titulo']), set(errors.keys()))
        self.assertEqual(old_properties, peca.key.get().to_dict())
        self.assert_can_render(template_response)
