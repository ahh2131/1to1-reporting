Reporting.factory('ReportingService', function ($http, $q) {
	return {
		menteeCalls: function(menteeId) {
			var defer = $q.defer();
			var url = "/mentee_calls/" + menteeId + "/";
			$http({method: 'POST', url: url}).
				success(function (data, status, headers, config) {
					defer.resolve(data);
				}).error(function (data, status, headers, config) {
					defer.reject(status);
				});
			return defer.promise;
			},
		listCalls: function() {
			var defer = $q.defer();
			$http({method: 'GET', url: '/dashboard/'}).
				success(function (data, status, headers, config) {
					defer.resolve(data);
				}).error(function (data, status, headers, config) {
					defer.reject(status);
				});
			return defer.promise;
			},
		listMentees: function() {
			var defer = $q.defer();
			$http({method: 'GET', url: '/mentees/'}).
				success(function (data, status, headers, config) {
					defer.resolve(data);
				}).error(function (data, status, headers, config) {
					defer.reject(status);
				});
			return defer.promise;
			},
		menteeInfo: function(menteeId) {
			var defer = $q.defer();
			var url = "/mentee/" + menteeId + "/";
			$http({method: 'POST', url: url}).
				success(function (data, status, headers, config) {
					defer.resolve(data);
				}).error(function (data, status, headers, config) {
					defer.reject(status);
				});
			return defer.promise;
			},
		}	
});