from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from db_access.models import Names
from rest_framework import viewsets
from db_access.serializers.drf_test import NamesSerializer


class NamesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Names.objects.all()
    serializer_class = NamesSerializer
