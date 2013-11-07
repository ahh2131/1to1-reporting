Reporting.factory('ReportingService', function ($http, $q) {
	return {
		list: function() {
			var defer = $q.defer();
			$http({method: 'GET', url: '/dashboard'}).
				success(function (data, status, headers, config) {
					defer.resolve(data);
				}).error(function (data, status, headers, config) {
					defer.reject(status);
				});
			return defer.promise;
		},
	}
});