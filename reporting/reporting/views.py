from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from reporting.models import Calls
from reporting.serializers import CallSerializer
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

class ReportingList(generics.ListCreateAPIView):
    """
    Lists all user info
    """
    model = Calls
    serializer_class = CallSerializer

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