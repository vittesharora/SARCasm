from django.shortcuts import render, get_object_or_404
from .models import Question
# Create your views here.

def home(request):
	return render(request, 'game/index.html',{})

def leaderboard(request):
	return render(request, 'game/leaderboard.html',{})

def instructions(request):
	return render(request, 'game/instructions.html',{})

def forum(request):
	return render(request, 'game/forum.html',{})

def prize(request):	
	return render(request, 'game/prize.html',{})

def play(request):
	return render(request, 'game/play.html',{})

def login(request):	
	return render(request, 'game/login.html',{})