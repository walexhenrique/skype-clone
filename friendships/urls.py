from django.urls import path

from . import views

app_name = 'friendships'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchListView.as_view(), name='search'),
    path('profile-detail/<slug:slug>/', views.ProfileDetailView.as_view(), name='profile-detail')
]
