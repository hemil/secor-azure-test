from rest_framework import serializers

from db_access.models import Names


class NamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Names
        fields = ['id', 'name']
