from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='homepage'),
    path('registration/', views.Registration.as_view(), name='register'),
    path('success/',views.SuccessView.as_view(), name='success')
]
