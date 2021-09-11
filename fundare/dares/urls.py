from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('dares/', views.DaresList.as_view()),
    path('dares/<int:pk>/', views.DaresDetail.as_view()),
    path('dollars/', views.DollarsList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)