from django.urls import path
from . import views

urlpatterns=[
path('',views.home, name='home'),
path('leaderboard',views.leaderboard, name='leaderboard'),
path('instructions', views.instructions, name='instructions'),
path('forum', views.forum, name='forum'),
path('prizes',views.prize, name='prize'),
path('play', views.play, name='play'),
path('login', views.login, name='login'),
]