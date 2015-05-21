# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from pecas_app.pecas_model import Peca
from routes.rests.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Peca)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        peca = mommy.save_one(Peca)
        redirect_response = delete(peca.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(peca.key.get())

    def test_non_peca_deletion(self):
        non_peca = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_peca.key.id())
        self.assertIsNotNone(non_peca.key.get())

