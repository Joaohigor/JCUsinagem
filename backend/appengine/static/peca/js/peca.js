var pecaModulo=angular.module('pecaModulo',[]);

pecaModulo.directive('pecaform',function(){
    return{
        restrict: 'E',
        replace:true,
        templateUrl:'/static/peca/html/peca_form.html',
        scope: {
            pecas: '=',
            titleLabel: '@',
            priceLabel: '@',
            amountLabel: '@',
            postNew: '='
        },
        controller:function($scope, $http){
            $scope.salvandoFlag=false;
            $scope.peca ={title: "Teste", price: "10", amount: "10"};
            $scope.salvar=function(peca){
                $scope.salvandoFlag=true;
                $scope.errors={};
                $http.post($scope.postNew, peca).success(function(pecas) {
                    console.log(pecas);
                    $scope.peca.title = '';
                    $scope.peca.price = '';
                    $scope.peca.amount = '';
                    $scope.salvandoFlag = false;
                    $scope.pecas.push(pecas);
                }).error(function (errors) {
                    $scope.errors = errors;
                    console.log(errors);
                    $scope.salvandoFlag = false;

                });
                //var promessa = PecasApi.salvar($scope.pecas);
                //promessa.success(function(pecas) {
                //        console.log(pecas);
                //        $scope.pecas.title = '';
                //        $scope.pecas.price = '';
                //        $scope.pecas.amount = '';
                //        $scope.salvandoFlag = false;
                //    })
                //promessa.error(function (errors) {
                //        $scope.errors = errors;
                //        console.log(errors);
                //        $scope.salvandoFlag = false;
                //
                //    });
            }
        }

    };
});
pecaModulo.directive('pecalinha',function(){
    return{
        replace:true,
        templateUrl:'/static/peca/html/peca_linha_tabela.html',
        scope: {
            pecas: '='
        },
        controller:function($scope){

        }

    };
});