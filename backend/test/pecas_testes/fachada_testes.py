# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from gaepermission.model import MainUser
from mommygae import mommy
from pecas_app import pecas_facade


class SalvarPecasTestes(GAETestCase):

    def teste_sucesso(self):
        usuario = mommy.save_one(MainUser)
        salvar_cmd = pecas_facade.save_peca_cmd(**{'title': 'Testando Teste', 'price': '3.44', 'amount': '23'})
        peca = salvar_cmd()

        listar_pecas_cmd = pecas_facade.list_pecas_cmd(usuario)
        pecas = listar_pecas_cmd()
        self.assertEqual(1, len(pecas))
        peca = pecas[0]
        self.assertEqual('Testando Teste', peca.title)
        self.assertEqual(float('3.44'), peca.price)
        self.assertEqual(int('23'), peca.amount)


    def teste_com_erros_validacao(self):

        usuario = mommy.save_one(MainUser)
        salvar_cmd = pecas_facade.save_peca_cmd()
        self.assertRaises(CommandExecutionException,salvar_cmd)
        erros=salvar_cmd.errors
        self.assertIn('title',erros)
        self.assertIn('price',erros)
        self.assertIn('amount',erros)
        # resposta = pecas_facade.save_peca_cmd(**{'title': '', 'price': '', 'amount': ''})
        # self.assertIsInstance(resposta, TemplateResponse)
        # self.assert_can_render(resposta)
        # self.assertDictEqual({'title':u'Required field','price':u'Required field','amount':u'Required field'}, resposta.context['errors'])