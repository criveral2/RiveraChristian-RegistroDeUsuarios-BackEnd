from django.urls import path

from apps.user.views import UserListCreateAPIView, UserApiView, CreateUserListCreateAPIView, CountriesListCreateAPIView

urlpatterns = [
    path('', UserListCreateAPIView.as_view()),
    path('nuevo', CreateUserListCreateAPIView.as_view()),
    path('<pk>', UserApiView.as_view()),
    path('countries/', CountriesListCreateAPIView.as_view()),
]