from django.db import models

class Mentor(models.Model):
	name = models.TextField(blank=True)

class Enrolling_Party(models.Model):
	name = models.TextField(blank=True)

class Mentee(models.Model):
	name = models.TextField(blank=True)
	enrolled_by = models.ForeignKey(Enrolling_Party)
	enrolled_on = models.DateField()

class Calls(models.Model):
	mentor_id = models.ForeignKey(Mentor)
	mentee_id = models.ForeignKey(Mentee)
	call_number = models.IntegerField()
	length = models.TimeField()
	start_time = models.TimeField()
	end_time = models.TimeField()
	date = models.DateTimeField(auto_now_add = False)
	num_completed_goals = models.IntegerField()
	num_active_goals = models.IntegerField()
	num_completed_action_plans = models.IntegerField()
	num_active_action_plans = models.IntegerField()
