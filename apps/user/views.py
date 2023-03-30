from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from apps.user.models import Users, Countries
from apps.user.serializers import UsersSerializer, CreateUsersSerializer, CountriesSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime


# Create your views here.
class UserListCreateAPIView(generics.ListCreateAPIView):
    user_serializer_class = UsersSerializer

    def list(self, request):
        queryset = Users.objects.all()
        users_serializer = self.user_serializer_class(queryset, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)


class CreateUserListCreateAPIView(generics.ListCreateAPIView):
    user_create_serializer_class = CreateUsersSerializer

    def create(self, request):
        if not self.mayor_edad(request.data["birth_date"]):
            return Response({"status": 404,"message": {"id": ["No puede ser menor de edad"]}}, status=status.HTTP_404_NOT_FOUND)

        user_serializer = self.user_create_serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"status": 200, "message": "success create", "data": user_serializer.data},
                            status=status.HTTP_200_OK)
        return Response({"status": 400, "message": user_serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    def mayor_edad(self, fecha):
        formato = "%Y-%m-%d"
        fecha = datetime.strptime(fecha, formato)
        duracion = datetime.now() - fecha
        anios = round(duracion.days / 365.25)
        return True if anios >= 18 else False;


class UserApiView(APIView):
    user_create_serializer_class = CreateUsersSerializer

    def put(self, request, pk=None):
        if not CreateUserListCreateAPIView.mayor_edad(self, request.data["birth_date"]):
            return Response({"status": 404, "message": {"id": ["No puede ser menor de edad"]}}, status=status.HTTP_404_NOT_FOUND)
        try:
            instance = get_object_or_404(Users, pk=pk)
            aux_id = instance.id
            users_serializer = self.user_create_serializer_class(instance, data=request.data, partial=True)
            if users_serializer.is_valid():
                users_serializer.save()
                if (aux_id != request.data["id"]):
                    delete = get_object_or_404(Users, pk=aux_id)
                    delete.delete()

                return Response({"status": 200, "message": "success update", "data": users_serializer.data},
                                status=status.HTTP_200_OK)
            return Response({"status": 400, "message": users_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"status": 400, "message": {"id": ["No existe el usuario con el id " + pk]}},
                            status=status.HTTP_400_BAD_REQUEST)


class CountriesListCreateAPIView(generics.ListCreateAPIView):
    countrie_serializer_class = CountriesSerializer

    def get(self, request):
        queryset = Countries.objects.all()
        countrie_serializer = self.countrie_serializer_class(queryset, many=True)
        return Response(countrie_serializer.data, status=status.HTTP_200_OK)
