from rest_framework import serializers
from reporting.models import Calls
from reporting.models import Mentee
from reporting.models import Enrolling_Party




class CallSerializer(serializers.ModelSerializer):
	class Meta:
		model = Calls
		fields = ('mentor_id', 'mentee_id', 'call_number', 'length', 'start_time',
			'end_time', 'date', 'num_completed_goals', 'num_active_goals', 
			'num_completed_action_plans', 'num_active_action_plans')

class EnrollingPartySerializer(serializers.ModelSerializer):
	owner = serializers.Field(source='owner.username')
	class Meta:
		model = Enrolling_Party
		fields = ('name', 'user')

class MenteeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mentee
		fields = ('id', 'name')
