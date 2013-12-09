Reporting.directive('timeAgo', function ($timeout) {
    return {
        restrict: 'A',
        scope: {
            title: '@'
        },
        link: function (scope, elem, attrs) {
            var updateTime = function () {
                if (attrs.title) {
                    elem.text(moment(attrs.title).fromNow());
                    $timeout(updateTime, 15000);
                }
            };
            scope.$watch(attrs.title, updateTime);
        }
    };
});

Reporting.directive('pendingBar', ['$rootScope',
    function ($rootScope) {
        return {
            link: function (scope, element, attrs) {
                element.addClass('hide');
                $rootScope.$on('$routeChangeStart', function () {
                    element.removeClass('hide');
                });
                $rootScope.$on('$routeChangeSuccess', function () {
                    element.addClass('hide');
                });
                $rootScope.$on('$routeChangeError', function () {
                    element.removeClass('hide');
                });
            }
        };
    }]);

Reporting.directive('ngMorrison', function() {
    return {
        //require: '^ngModel',
        scope: {
          ngModel: '='
        },
        template: '<div id="call-chart" class="graph">test</div>',
        controller: ['$scope', '$http', '$q', function($scope, $http, $q) {
          $scope.getCalls = function() {
            var defer = $q.defer();
            $http({method: 'GET', url: '/dashboard/'}).
                success(function (data, status, headers, config) {
                    defer.resolve(data);
                }).error(function (data, status, headers, config) {
                    defer.reject(status);
                });
            return defer.promise;
          }
        }],
        link: function(scope, iElement, iAttrs, ctrl) {
            calls = scope.getCalls();
            // get list of users
            new Morris.Line({
              // ID of the element in which to draw the chart.
              element: iElement,
              // Chart data records -- each entry in this array corresponds to a point on
              // the chart.
              data: [
                { year: '2008', value: 20 },
                { year: '2009', value: 10 },
                { year: '2010', value: 5 },
                { year: '2011', value: 5 },
                { year: '2012', value: 20 }
              ],
              // The name of the data record attribute that contains x-values.
              xkey: '{year}',
              // A list of names of data record attributes that contain y-values.
              ykeys: ['value'],
              // Labels for the ykeys -- will be displayed when you hover over the
              // chart.
              labels: ['Value']
            });
        }
    };
});

Reporting.directive('morrisLine', function(){
  return {
    restrict: 'EA',
    template: '<div id="call-chart">tet2</div>',
    scope: {
        data: '=', //list of data object to use for graph
        xkey: '=',
        ykey: '='
    },
    link: function(scope,element,attrs){
      new Morris.Line({
          element: "call-chart",
          data: [
                { year: '2008', value: 20 },
                { year: '2009', value: 10 },
                { year: '2010', value: 5 },
                { year: '2011', value: 5 },
                { year: '2012', value: 20 }
              ],
          xkey: '{year}',
          ykey: ['value'],
      });
   }
  };
});

Reporting.directive('viewState', ['$rootScope',
    function ($rootScope) {
        return {
            link: function (scope, element, attrs) {
                element.addClass('hide');
                $rootScope.$on('$routeChangeStart', function () {
                    element.addClass('hide');
                });
                $rootScope.$on('$routeChangeSuccess', function () {
                    element.removeClass('hide');
                });
                $rootScope.$on('$routeChangeError', function () {
                    element.addClass('hide');
                });
            }
        };
    }]);

 /*<script>
  console.log("test");
  new Morris.Line({
    // ID of the element in which to draw the chart.
    element: 'call-chart',
    // Chart data records -- each entry in this array corresponds to a point on
    // the chart.
    data: [
      { year: '2008', value: 20 },
      { year: '2009', value: 10 },
      { year: '2010', value: 5 },
      { year: '2011', value: 5 },
      { year: '2012', value: 20 }
    ],
    // The name of the data record attribute that contains x-values.
    xkey: '{year}',
    // A list of names of data record attributes that contain y-values.
    ykeys: ['value'],
    // Labels for the ykeys -- will be displayed when you hover over the
    // chart.
    labels: ['Value']
  });
  </script> -->
  */