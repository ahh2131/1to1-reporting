from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from reporting.models import Calls
from reporting.models import Mentee
from reporting.models import Enrolling_Party
from reporting.serializers import CallSerializer
from reporting.serializers import EnrollingPartySerializer
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

"""
delete below before deploying
class ReportingList(generics.ListCreateAPIView):
    
    
    Lists all user info
    
    model = Enrolling_Party
    serializer_class = EnrollingPartySerializer
    def pre_save(self, obj):
        obj.owner = self.request.user
"""
class LoginFormView(TemplateView):
    template_name = 'signin.html'


def home(request, template_name="index2.html"):
    """
    A index view.
    """
    return render_to_response(template_name,
                              context_instance=RequestContext(request))

def profile(request, template_name=""):
    """
    A index view.
    """
    return render_to_response(template_name,
                              context_instance=RequestContext(request))
def signin(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/#/dashboard')
    else:
        return HttpResponseRedirect('/login')

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
    enrolling_party = Enrolling_Party.objects.get(user=request.user.id)
    mentee = Mentee.objects.get(enrolled_by_id=enrolling_party.id)
    calls = Calls.objects.filter(mentee_id_id=mentee.id)
    serializer = CallSerializer(calls, many=True)
    return JSONResponse(serializer.data)
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
    """