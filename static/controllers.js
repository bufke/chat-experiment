var app = angular.module('ChatControllers', ['restangular']);

app.factory('ChatStatus', function() {
    var data = {
        selectedRoom: 1,
        messages: {}
    };
    return data;
});


app.controller('ChatRoomCtrl',
        ['$scope', '$dragon', 'ChatStatus', 'Users', function (
            $scope, $dragon, ChatStatus, Users) {
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
    });

    $dragon.onChannelMessage(function(channels, message) {
        if (indexOf.call(channels, $scope.channel) > -1) {
            if (ChatStatus.messages[message.data.room].indexOf(message.data) == -1) {
                message.data.posted = new Date(message.data.posted);
                $scope.$apply(function() {
                    ChatStatus.messages[message.data.room].push(message.data);
                });
            }
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


app.controller('RoomCtrl', ['$scope', 'Rooms', 'Messages', 'ChatStatus', function($scope, Rooms, Messages, ChatStatus) {
    $scope.changeRoom = function(room) {
        ChatStatus.selectedRoom = room;
        Messages.getList({'room': room.id}).then(function(messages) {
            angular.forEach(messages, function(message, key) {
                message.posted = new Date(message.posted);
            });
            ChatStatus.messages[room.id] = messages;
        });
    }
    $scope.rooms = Rooms.getList()
    .then(function(rooms) {
        ChatStatus.rooms = rooms;
        ChatStatus.selectedRoom = rooms[0];
        $scope.rooms = rooms;
    })
}]);

app.factory('Users', ['Restangular', function(Restangular) {
    return Restangular.service('users');
}]);
app.factory('Rooms', ['Restangular', function(Restangular) {
    return Restangular.service('rooms');
}]);
app.factory('Messages', ['Restangular', function(Restangular) {
    return Restangular.service('messages');
}]);
