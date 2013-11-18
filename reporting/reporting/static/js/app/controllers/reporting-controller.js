Reporting.controller('ReportingController', function ($scope, GlobalService, ReportingService, calls, mentees) {
	$scope.globals = GlobalService;
	$scope.mentees = mentees;
	// combines names to calls array
	for (var i=0;i<calls.length;i++){
		for (var j=0;j<mentees.length;j++){
			if (mentees[j].id == calls[i].mentee_id){
				calls[i].mentee_id = mentees[j].name
			}
		}
	}
	$scope.calls = calls;


});