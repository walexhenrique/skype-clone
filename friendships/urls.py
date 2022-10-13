from django.urls import path

from . import views

app_name = 'friendships'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchListView.as_view(), name='search'),
    path('pending/', views.FriendsPendingView.as_view(), name='pending'),
    path('profile-denied/<int:id>/', views.DeniedRequestView.as_view(), name='profile-denied'),
    path('profile-detail/<slug:slug>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profile-detail/<slug:slug>/edit/', views.ProfileEditUpdateView.as_view(), name='profile-edit'),
    path('friend-request/<slug:slug>/', views.ProfileFriendRequest.as_view(), name='friend-request'),
]
