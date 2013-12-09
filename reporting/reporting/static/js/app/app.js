'use strict';
// new start symbol and end symbol to differentiate from django's
// dependency on bootstrap ui, an angular directive
var Reporting = angular.module("Reporting", ["ui.bootstrap", "ngCookies", "dangle"], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    }
);
// sets up a csrf token
Reporting.run(function ($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
})

// routing for our app
// uses resolve , which loads data before changing the view, providing a better
// user experience, no waiting for the data to load
Reporting.config(function ($routeProvider) {
    $routeProvider
        .when("/", {
            // template
            templateUrl: "static/js/app/views/feed.html",
            // contains functions which can be called from the template
            controller: "FeedController",
            resolve: {
                // returns an object called 'post' which can be referenced
                // in the template using {[{ posts[0].title }]}
                posts: function (PostService) {
                    // returns object of posts using posts service
                    return PostService.list();
                }
            }
        })
        .when("/dashboard", {
            templateUrl: "static/js/app/views/dashboard.html",
            controller: "ReportingController",
            resolve: {
                calls: function(ReportingService) {
                    return ReportingService.listCalls();
                },
                mentees: function(ReportingService) {
                    return ReportingService.listMentees();
                }
            }
        })
        .when("/profile/:id", {
            // template
            templateUrl: "static/js/app/views/profile.html",
            // containsprofile functions which can be called from the template
            controller: "ProfileController",
            resolve: {
                mentee_calls: function ($route, ReportingService){
                    var menteeId = $route.current.params.id
                    return ReportingService.menteeCalls(menteeId);
                },
                mentee_info: function($route, ReportingService){
                    var menteeId = $route.current.params.id
                    return ReportingService.menteeInfo(menteeId);
                }
            }

        })
        .when("/post/:id", {
            templateUrl: "static/js/app/views/view.html",
            controller: "PostController",
            resolve: {
                post: function ($route, PostService) {
                    var postId = $route.current.params.id
                    return PostService.get(postId);
                }
            }
        })

        .otherwise({
            redirectTo: '/'
        })


})