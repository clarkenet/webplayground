from django.urls import path
from .views import ProfileListView, ProfileDetailView

profile_patterns = ([
    path('', ProfileListView.as_view(), name='profile_list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
], 'profiles')
