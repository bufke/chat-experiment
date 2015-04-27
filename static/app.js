var ChatApp = angular.module('ChatApp', [
    'SwampDragonServices',
    'ChatControllers',
    'ngRoute',
]);

function get_static(path) {
    return STATIC_URL + path;
}

ChatApp.config(function($routeProvider, $locationProvider) {
    $routeProvider.when("/", {
        controller: "ChatRoomCtrl",
        templateUrl: get_static("/partials/chatroom.html")
  });
});

ChatApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

ChatApp.config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl("/api");
    RestangularProvider.setRequestSuffix("/");
});
