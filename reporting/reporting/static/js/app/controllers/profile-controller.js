Reporting.controller('ProfileController', function ($scope, GlobalService, ReportingService, mentee_calls, mentee_info) {
	$scope.globals = GlobalService;
	$scope.mentee_calls = mentee_calls;
	$scope.mentee_info = mentee_info;
	$scope.display_call = 0;

	var j = 0;
	year = null;
	day = null;
	month = null;
	// calculates total number of mentee_calls each day
	// assumes mentee_calls are in order
	var entries = [];
	while(j<mentee_calls.length){
		old_year = year;
		old_day = day;
		old_month = month;
		year = mentee_calls[j].date.substring(0, 4);
		month = mentee_calls[j].date.substring(5, 7);
		day = mentee_calls[j].date.substring(8, 10);
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