# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaebusiness.business import Command, CommandParallel, CommandExecutionException
from gaecookie.decorator import no_csrf
from config.template_middleware import TemplateResponse
from gaeforms import base
from gaeforms.base import Form
from gaeforms.ndb.form import ModelForm
from tekton import router
from gaegraph.model import Node
from tekton.gae.middleware.redirect import RedirectResponse
from gaegraph.model import Arc
from gaepermission.decorator import login_required
from gaepermission.decorator import login_not_required

@no_csrf
def index(_logged_user):
    chave_do_usuario=_logged_user.key
    query = PecasArco.query(PecasArco.origin==chave_do_usuario)
    peca_arco=query.fetch()
    chaves_de_pecas=[arco.destination for arco in peca_arco]

    peca_lista = filter(None, ndb.get_multi(chaves_de_pecas))

    peca_form = PecaFormTable()
    peca_lista=[peca_form.fill_with_model(pecas) for pecas in peca_lista]
    editar_form_path=router.to_path(editar_form)
    delete_path=router.to_path(delete)
    for pecas in peca_lista:
        pecas['edit_path']='%s/%s'%(editar_form_path,pecas['id'])
        pecas['delete_path']='%s/%s'%(delete_path,pecas['id'])
    contexto={'peca_lista': peca_lista,
              'form_path':router.to_path(form)}
    return TemplateResponse(contexto)

@login_required
def delete(pecas_id):
    chave=ndb.Key(Peca,int(pecas_id))
    chave.delete()
    return RedirectResponse(router.to_path(index))

@login_required
@no_csrf
def editar_form(pecas_id):
    pecas_id=int(pecas_id)
    pecas=Peca.get_by_id(pecas_id)
    pecas_form=PecaForm()
    pecas_form.fill_with_model(pecas)
    contexto = {'salvar_path': router.to_path(editar, pecas_id),
                'pecas':pecas_form}
    return TemplateResponse(contexto, 'pecas/form.html')

@login_required
def editar(pecas_id,**propriedades):
    pecas_id = int(pecas_id)
    pecas=Peca.get_by_id(pecas_id)
    peca_form = PecaForm(**propriedades)
    erros = peca_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'erros':erros,
                    'pecas':peca_form}
        return TemplateResponse(contexto, 'pecas/form.html')
    else:
         peca_form.fill_model(pecas)
         pecas.put()
         return RedirectResponse(router.to_path(index))

@login_required
@no_csrf
def form():
    contexto = {'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)

class Peca(Node):
    title = ndb.StringProperty(required=True)
    price = ndb.FloatProperty()
    amount = ndb.IntegerProperty()

class PecasArco(Arc):
    origin = ndb.KeyProperty(required=True)
    destination = ndb.KeyProperty(Peca,required=True)


class PecaFormTable(ModelForm):
    _model_class = Peca
    _include = [Peca.title,Peca.price,Peca.amount,Peca.creation]


class PecaForm(ModelForm):
    _model_class = Peca
    _include = [Peca.title,Peca.price,Peca.amount]

    #title = base.StringField(required=True)
    #price=base.FloatField()
    #amount=base.IntegerField()

@login_required
def salvar(_logged_user,**propriedades):
    peca_form = PecaForm(**propriedades)
    erros = peca_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'erros':erros,
                    'pecas':peca_form}
        return TemplateResponse(contexto, 'pecas/form.html')
    else:
         peca = peca_form.fill_model()
         chave_da_peca= peca.put()
         chave_de_usuario=_logged_user.key
         peca_arco=PecasArco(origin=chave_de_usuario,destination=chave_da_peca)
         peca_arco.put()

         return RedirectResponse(router.to_path(index))