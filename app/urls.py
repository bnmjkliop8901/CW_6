from django.urls import path

from app.views import TaskDetailSerializers , TaskCreateSerializers , UserDetailSerializers , UserCreateSerializers

from .views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('tasks/' , TaskCreateSerializers.as_view()),
    path('tasks/<int:pk>/' , TaskDetailSerializers.as_view()),

    path('people/' , UserCreateSerializers.as_view()),
    path('people/<int:pk>/' , UserDetailSerializers.as_view()),

    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

