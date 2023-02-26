
from rest_framework import serializers
from employeeapp.models import Company

#create serializers here
#apiadd

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model=Company
        fields="__all__"
