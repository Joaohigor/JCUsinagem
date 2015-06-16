# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
from base import GAETestCase
from pecas_app.pecas_model import Peca
from mommygae import mommy

class PecasTestes(GAETestCase):
    def teste_salvar_peca(self):
        peca=mommy.make_one(Peca, title='Testando Teste')
        peca.put()
        pecas_em_bd=peca.query_by_creation().fetch()
        self.assertListEqual([peca], pecas_em_bd)
        self.assertEqual('Testando Teste', pecas_em_bd[0].title)