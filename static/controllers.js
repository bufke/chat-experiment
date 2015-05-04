var app = angular.module('ChatControllers', ['restangular']);

app.factory('ChatStatus', function() {
    var data = {
        selectedRoom: 1
    };
    return data;
});


app.controller('ChatRoomCtrl',
        ['$scope', '$dragon', 'ChatStatus', 'Users', function (
            $scope, $dragon, ChatStatus, Users) {
    $scope.messages = [];
    $scope.channel = 'messages';
    $scope.ChatStatus = ChatStatus;
    
    $scope.idToUser = function(id) {
        var user;
        user = $scope.users.filter(function(obj) {
            return obj.pk == id;
        });
        return user[0].display_name;
    };
    Users.getList().then(function(users) {
        $scope.users = users;
    });

    $dragon.onReady(function() {
        $dragon.subscribe('messages', $scope.channel).then(function(response) {
            $scope.dataMapper = new DataMapper(response.data);
        });
        $dragon.getList('messages').then(function(response) {
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
        '$scope', 'Messages', 'ChatStatus', function(
            $scope, Messages, ChatStatus) {
    $scope.sendForm = {};
    $scope.sendForm.text = '';
    $scope.sendForm.submit = function() {
        var data = {
            "room": ChatStatus.selectedRoom.id,
            "text": $scope.sendForm.text
        } 
        Messages.post(data).then(function() {
            $scope.sendForm.text = '';
        }, function(error) {
            $scope.status = 'error';
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

app.factory('Users', ['Restangular', function(Restangular) {
    return Restangular.service('users');
}]);
app.factory('Messages', ['Restangular', function(Restangular) {
    return Restangular.service('messages');
}]);
