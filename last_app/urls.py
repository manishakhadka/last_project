

from django.urls import path
from .views import CustomUserListView, CustomUserDetailView

urlpatterns = [
    path('', CustomUserListView.as_view()),
    path('<int:pk>/', CustomUserDetailView.as_view()),
]
