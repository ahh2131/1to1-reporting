Reporting.controller('ReportingController', function ($scope, GlobalService, ReportingService, calls) {
	$scope.globals = GlobalService;
	$scope.calls = calls;
});