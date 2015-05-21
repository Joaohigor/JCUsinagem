# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime, date
from decimal import Decimal
from base import GAETestCase
from pecas_app.pecas_model import Peca
from routes.rests import rest
from gaegraph.model import Node
from mock import Mock
from mommygae import mommy


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Peca)
        mommy.save_one(Peca)
        json_response = rest.index()
        context = json_response.context
        self.assertEqual(2, len(context))
        peca_dct = context[0]
        self.assertSetEqual(set(['id', 'creation', 'titulo']), set(peca_dct.iterkeys()))
        self.assert_can_serialize_as_json(json_response)


class NewTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Peca.query().get())
        json_response = rest.new(None, titulo='titulo_string')
        db_peca = Peca.query().get()
        self.assertIsNotNone(db_peca)
        self.assertEquals('titulo_string', db_peca.titulo)
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        resp = Mock()
        json_response = rest.new(resp)
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['titulo']), set(errors.keys()))
        self.assert_can_serialize_as_json(json_response)


class EditTests(GAETestCase):
    def test_success(self):
        peca = mommy.save_one(Peca)
        old_properties = peca.to_dict()
        json_response = rest.edit(None, peca.key.id(), titulo='titulo_string')
        db_peca = peca.key.get()
        self.assertEquals('titulo_string', db_peca.titulo)
        self.assertNotEqual(old_properties, db_peca.to_dict())
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        peca = mommy.save_one(Peca)
        old_properties = peca.to_dict()
        resp = Mock()
        json_response = rest.edit(resp, peca.key.id())
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['titulo']), set(errors.keys()))
        self.assertEqual(old_properties, peca.key.get().to_dict())
        self.assert_can_serialize_as_json(json_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        peca = mommy.save_one(Peca)
        rest.delete(None, peca.key.id())
        self.assertIsNone(peca.key.get())

    def test_non_peca_deletion(self):
        non_peca = mommy.save_one(Node)
        response = Mock()
        json_response = rest.delete(response, non_peca.key.id())
        self.assertIsNotNone(non_peca.key.get())
        self.assertEqual(500, response.status_code)
        self.assert_can_serialize_as_json(json_response)

