var ChatControllers = angular.module('ChatControllers', ['restangular']);

ChatControllers.controller('ChatCtrl', ['$scope', '$dragon', function ($scope, $dragon) {
    $scope.messages = [];
    $scope.channel = 'messages';

    $dragon.onReady(function() {
        $dragon.subscribe('messages', $scope.channel).then(function(response) {
            $scope.dataMapper = new DataMapper(response.data);
        });
        $dragon.getList('messages', {list_id:1}).then(function(response) {
            $scope.messages = response.data;
        });
    });

    $dragon.onChannelMessage(function(channels, message) {
        if (indexOf.call(channels, $scope.channel) > -1) {
            $scope.$apply(function() {
                $scope.dataMapper.mapData($scope.messages, message);
            });
        }
    });
}]);


ChatControllers.controller('SendChatCtrl', ['$scope', '$http', function($scope, $http) {
    $scope.sendForm = {};
    $scope.sendForm.text = '';
    $scope.sendForm.submit = function() {
        var data = {
            "room": 1,
            "text": $scope.sendForm.text
        } 
        $http.post("/api/messages/", data)
        .success(function(data, status, headers, config) {
                $scope.sendForm.text = '';
        }).error(function(data, status, headers, config) {
                $scope.status = status;
        });
    };
}]);


ChatControllers.controller('RoomCtrl', ['$scope', 'Restangular', function($scope, Restangular) {
    $scope.rooms = Restangular.all('rooms').getList().$object;
}]);
