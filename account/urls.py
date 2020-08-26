# account/urls.py

from django.urls import path
from account import views

urlpatterns = [
	# postviews
	path('login/', views.user_login, name='login')
]