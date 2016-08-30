import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from organisation.models import Organisation
from organisation.serializers import UserSerializer, OrganisationSerializer


def home(request):
    return render(request, 'index.html')


@api_view(['GET'])
def organisation_details(request):
    if request.method == 'GET':
        org_id = request.GET.get('org_id', None)
        if org_id:
            try:
                org = Organisation.objects.get(pk=org_id)
            except(Organisation.DoesNotExist, ValueError, Organisation.MultipleObjectsReturned):
                return HttpResponse('{No Data Found, Please Enter Valid Org ID}')
            org_team = org.org_team.all().exclude(parent_team__isnull=False)
            return render(request, template_name='org_temp.html', context={'org': org, 'org_team': org_team})
        else:
            org = Organisation.objects.all()
            serializer = OrganisationSerializer(org, many=True)
            return Response(serializer.data)


@api_view(['GET'])
@login_required
def user_list(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id', None)
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
            except(User.DoesNotExist, ValueError, User.MultipleObjectsReturned):
                return HttpResponse('{No Data Found, Seems You Have lost your way}')
            return render(request, template_name='user_temp.html', context={'user': user, 'admin': user.is_superuser})
        else:
            user = request.user
            serializer = UserSerializer(user)
            return Response(serializer.data)