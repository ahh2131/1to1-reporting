Reporting.controller('ReportingController', function ($scope, GlobalService, ReportingService, users) {
	$scope.globals = GlobalService;
	$scope.users = users;
})