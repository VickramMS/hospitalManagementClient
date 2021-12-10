from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('analytics/<id>', views.AnalyticsView.as_view()),
    path('newPatient', views.NewPatient.as_view()),

    #api

    path('api/analytics/<id>', api.AnalyticsAPI.as_view()),
    path('api/update', api.UpdateDataAPI.as_view())
]
