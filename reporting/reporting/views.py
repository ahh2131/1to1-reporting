from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from reporting.models import Calls
from reporting.serializers import CallSerializer


from django.shortcuts import render_to_response
from django.template import RequestContext

class ReportingList(generics.ListCreateAPIView):
    """
    Lists all user info
    """
    model = Calls
    serializer_class = CallSerializer

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