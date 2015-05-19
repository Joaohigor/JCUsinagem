var pecaModulo=angular.module('pecaModulo',['rest']);

pecaModulo.directive('pecaform',function(){
    return{
        restrict: 'E',
        replace:true,
        templateUrl:'/static/peca/html/peca_form.html',
        scope: {
            pecas: '=',
            titleLabel: '@',
            priceLabel: '@',
            amountLabel: '@'
        },
        controller:function($scope, PecasApi){
            $scope.salvandoFlag=false;
            $scope.salvar=function(){
                $scope.salvandoFlag=true;
                $scope.errors={};
                var promessa = PecasApi.salvar($scope.pecas);
                promessa.success(function(pecas) {
                        console.log(pecas);
                        $scope.pecas.title = '';
                        $scope.pecas.price = '';
                        $scope.pecas.amount = '';
                        $scope.salvandoFlag = false;
                    })
                promessa.error(function (errors) {
                        $scope.errors = errors;
                        console.log(errors);
                        $scope.salvandoFlag = false;

                    });
                }
        }

    };
});
pecaModulo.directive('pecalinha',function(){
    return{
        restrict: 'A',
        replace:true,
        templateUrl:'/static/peca/html/peca_linha_tabela.html',
        scope: {
            pecas: '='
        },
        controller:function($scope, PecasApi){

        }

    };
});