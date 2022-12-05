from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='homepage'),
    path('registration/', views.Registration.as_view(), name='register'),
    path('success/',views.SuccessView.as_view(), name='success'),
    path('status/',views.StatusView.as_view(),name='status'),
    path('login',views.LoginView.as_view(),name='login'),
]
