/**
 * Created by joao on 18/05/15.
 */
        var rest=angular.module('rest',[]);
        rest.factory('PecasApi',function($http){
           return{
               salvar: function(pecas){
                   var obj={};
                   obj.success=function(fncSucesso){
                       obj.fncSucesso=fncSucesso;
                   };
                   obj.error=function(fncErro){
                       obj.fcnError=fncErro;
                   };

                   setTimeout(function(){
                       peca.id=1;
                       obj.fncSucesso(pecas)
                       $rootScope.$digest();
                   },1000);

                   return obj;
               }
           };
        });