from rest_framework import serializers
from apps.user.models import Countries, Users


class CountriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Countries
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    country = CountriesSerializer()
    class Meta:
        model = Users
        fields = '__all__'


class CreateUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

