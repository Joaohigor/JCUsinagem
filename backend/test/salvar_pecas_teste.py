# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from config.template_middleware import TemplateResponse
from pecas_app.pecas_model import Peca
from routes.rests import rest
from tekton.gae.middleware.redirect import RedirectResponse


class SalvarTestes(GAETestCase):
    def teste_sucesso(self):
        resposta = rest.new(_logged_user={},peca_properties={"title":"teste"})
        self.assertIsInstance(resposta, RedirectResponse)
        peca=Peca.query().get()
        self.assertIsNone(peca)
        self.assertEqual('teste', peca.titulo)

    def teste_erros_validacao(self):
        resposta = rest.new(title='')
        self.assertIsInstance(resposta, TemplateResponse)
        self.assert_can_render(resposta)
        self.assertDictEqual({},resposta.context['errors'])