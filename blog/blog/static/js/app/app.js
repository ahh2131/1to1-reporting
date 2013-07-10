'use strict';

var Blog = angular.module("Blog", ["ui.bootstrap", "ngResource", "ngCookies"], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    }
);

Blog.run(function ($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
})

Blog.config(function ($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "static/js/app/views/feed.html",
            controller: "FeedController",
            resolve: {
                posts: function (PostService) {
                    return PostService.list();
                }
            }
        })
        .when("/post/:id", {
            templateUrl: "static/js/app/views/posts/view.html",
            controller: "PostController",
            resolve: {
                post: function ($route, PostService) {
                    var postId = $route.current.params.id
                    return BoardService.get(postId);
                }
            }
        })
        .otherwise({
            redirectTo: '/'
        })
})