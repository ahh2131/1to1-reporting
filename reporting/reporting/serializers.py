from rest_framework import serializers
from reporting.models import Calls
from reporting.models import Enrolling_Party
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



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

# renders any data into JSON
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def call_list(request):
    """
    Lists users calls
    """
    if request.method == 'GET':
        calls = Calls.objects.all()
        serializer = CallSerializer(calls, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)