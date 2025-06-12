from django.urls import path

from app.views import TaskDetailSerializers , TaskCreateSerializers , PeopleCreateSerializers , PeopleDetailSerializers

from .views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('task/' , TaskCreateSerializers.as_view()),
    path('task/<int:pk>/' , TaskDetailSerializers.as_view()),

    path('people/' , PeopleCreateSerializers.as_view()),
    path('people/<int:pk>/' , PeopleDetailSerializers.as_view()),

    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

