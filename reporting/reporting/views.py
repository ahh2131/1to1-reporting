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
from reporting.serializers import MenteeSerializer
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
from itertools import chain


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

# def call_list(request):
#     """
#     Lists users calls
#     """
#     enrolling_party = Enrolling_Party.objects.get(user=request.user.id)
#     mentee = Mentee.objects.filter(enrolled_by_id=enrolling_party.id)
#     mentee_list = list(mentee)
#     result_query = set()
#     for mentee in mentee_list:
#         calls = Calls.objects.filter(mentee_id_id=mentee.id).order_by('-date')
#         name = Mentee.objects.filter(id=mentee.id)
#         result_query = chain(calls, result_query)
#     serializer = CallSerializer(result_query, many=True)
#     return JSONResponse(serializer.data)

def call_list(request):
    """
    new and improved call list
    list users calls
    """
    enrolling_party = Enrolling_Party.objects.get(user=request.user.id)
    calls = Calls.objects.filter(mentee_id__enrolled_by__exact=enrolling_party).order_by('-date')
    serializer = CallSerializer(calls, many=True)
    return JSONResponse(serializer.data)

def mentee_list(request):
    """
    lists mentees of users
    """
    enrolling_party = Enrolling_Party.objects.get(user=request.user.id)
    mentee = Mentee.objects.filter(enrolled_by_id=enrolling_party.id)
    serializer = MenteeSerializer(mentee, many=True)
    return JSONResponse(serializer.data)

def mentee_calls(request, pk):
    enrolling_party = Enrolling_Party.objects.get(user=request.user.id)
    mentee = Mentee.objects.get(enrolled_by_id=enrolling_party.id, id=pk)
    calls = Calls.objects.filter(mentee_id_id=mentee.id).order_by('-date')

    serializer = CallSerializer(calls, many=True)
    return JSONResponse(serializer.data)

def mentee_info(request, pk):
    enrolling_party = Enrolling_Party.objects.get(user=request.user.id)
    mentee = Mentee.objects.filter(enrolled_by_id=enrolling_party.id, id=pk)
    serializer = MenteeSerializer(mentee)
    return JSONResponse(serializer.data)


