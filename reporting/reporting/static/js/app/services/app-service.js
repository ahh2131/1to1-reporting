// allows for communication between controllers and global variables
Reporting.factory('GlobalService', function () {
    var vars = {
        is_authenticated: false
    }
	return vars;
});