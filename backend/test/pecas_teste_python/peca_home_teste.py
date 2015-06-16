# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from mommygae import mommy
from pecas_app.pecas_model import Peca
from routes import pecas


class HomeTests(GAETestCase):
    def test_index(self):
        mommy.save_one(Peca)
        resposta = pecas.index()
        self.assert_can_render(resposta)

