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


	var j = 0;
	year = null;
	day = null;
	month = null;
	// calculates total number of calls each day
	// assumes calls are in order
	var entries = [];
	while(j<calls.length){
		old_year = year;
		old_day = day;
		old_month = month;
		year = calls[j].date.substring(0, 4);
		month = calls[j].date.substring(5, 7);
		day = calls[j].date.substring(8, 10);
		if (old_year == year && old_month == month && old_day == day){
			obj.count += 1;
		}
		else {
			if (obj) entries.push(obj);
			var obj = {
				time: new Date(year, day, month),
				count: 1
			};
		}
		j += 1;
	}
	entries.push(obj);

	$scope.graph = {
		entries: entries
	};

});