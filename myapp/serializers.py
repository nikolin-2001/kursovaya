from rest_framework import serializers
from .models import Discipline

class DisciplineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Discipline
        fields = ('name', 'description','total','average')
