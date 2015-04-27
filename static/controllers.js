var app = angular.module('ChatControllers', ['restangular']);

app.factory('ChatStatus', function() {
    var data = {
        selectedRoom: 1
    };
    return data;
});


app.controller('ChatRoomCtrl',
        ['$scope', '$dragon', 'ChatStatus', function (
            $scope, $dragon, ChatStatus) {
    $scope.messages = [];
    $scope.channel = 'messages';
    $scope.ChatStatus = ChatStatus;

    $dragon.onReady(function() {
        $dragon.subscribe('messages', $scope.channel).then(function(response) {
            $scope.dataMapper = new DataMapper(response.data);
        });
        $dragon.getList('messages', {list_id: 1}).then(function(response) {
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


app.controller('SendChatCtrl', [
        '$scope', '$http', 'ChatStatus', function(
            $scope, $http, ChatStatus) {
    $scope.sendForm = {};
    $scope.sendForm.text = '';
    $scope.sendForm.submit = function() {
        var data = {
            "room": ChatStatus.selectedRoom.id,
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


app.controller('RoomCtrl', ['$scope', 'Restangular', 'ChatStatus', function($scope, Restangular, ChatStatus) {
    $scope.changeRoom = function(room) {
        ChatStatus.selectedRoom = room;
    }
    $scope.rooms = Restangular.all('rooms').getList()
    .then(function(rooms) {
        ChatStatus.rooms = rooms;
        ChatStatus.selectedRoom = rooms[0];
        $scope.rooms = rooms;
    })
}]);
