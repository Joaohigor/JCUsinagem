var pecaModule = angular.module('pecaModule',['rest']);
pecaModule.directive('pecaform',function(){
    return {
        restrict: 'E',
        replace: true,
        templateUrl: '/static/peca/html/peca_form.html',
        scope:{
            peca:'=',
            saveComplete:'&'
        },
        controller:function($scope, PecaApi){
            $scope.salvandoFlag=false;
            $scope.salvar=function(){
                $scope.salvandoFlag=true;
                $scope.errors={};
                var promessa = PecaApi.salvar($scope.peca);
                promessa.success(function(peca){
                    $scope.salvandoFlag=false;
                    $scope.peca.title = "";
                    $scope.peca.price = "";
                    $scope.peca.amount = "";
                    if($scope.saveComplete != undefined) {
                        $scope.saveComplete({'peca':peca});
                    }
                })
                promessa.error(function (errors) {
                    $scope.errors = errors;
                    $scope.salvandoFlag=false;

                });

            }
        }
    };
});

pecaModule.directive('pecalinha',function(){
    return {
        restrict: 'A',
        replace: true,
        templateUrl: '/static/peca/html/peca_linha_tabela.html',
        scope:{
            peca: '=',
            deleteComplete: '&'
        },
        controller:function($scope, PecaApi){
            $scope.ajaxFlag=false;
            $scope.editandoFlag=false;
            $scope.pecaEdicao={}
            $scope.deletar=function(){
                PecaApi.deletar($scope.peca.id).success(function(){
                    $scope.ajaxFlag=true;
                    $scope.deleteComplete({'peca':$scope.peca});
                });
            };
            $scope.editar=function(){
                    $scope.editandoFlag=true;
                    $scope.pecaEdicao.id=$scope.peca.id;
                    $scope.pecaEdicao.title=$scope.peca.title;
                    $scope.pecaEdicao.price=$scope.peca.price;
                    $scope.pecaEdicao.amount=$scope.peca.amount;
            };
            $scope.cancelar=function(){
                $scope.editandoFlag=false;
            };

            $scope.completarEdicao=function(){
                PecaApi.editar($scope.pecaEdicao).success(function(peca){
                    $scope.peca=peca;
                    $scope.editandoFlag=false;
                });
            }
        }

    };
});