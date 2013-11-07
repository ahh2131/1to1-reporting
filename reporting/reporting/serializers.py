from rest_framework import serializers
from reporting.models import Calls

class CallSerializer(serializers.HyperlinkedModelSerializer):
	api_url = serializers.SerializerMethodField('get_api_url')
	class Meta:
		model = Calls
		fields = ('mentor_id', 'mentee_id', 'call_number', 'length', 'start_time',
			'end_time', 'date', 'num_completed_goals', 'num_active_goals', 
			'num_completed_action_plans', 'num_active_action_plans')
	def get_api_url(self, obj):
		return "#/dashboard"