# acccount/views.py

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from account.forms import LoginForm
from django.contrib.auth.decorators import login_required


 # The login_required decorator checks if the current user is authenticated or not
 # If current user is authenticated, it executes the decorated view
 # If current user is NOT authenticated, it will redirect to login
@login_required
def dashboard(request):
	return render(request, 'account/dashboard.html', {'section':'dashboard'})


def user_login(request):

	# A. IF USER SENT POST REQUEST (TRY TO LOG IN)
	
	#1 If a user sent a post request to login
	if request.method == 'POST':
		#2 Let the user fillin the form
		form = LoginForm(request.POST)
		
		# IF USER EXISTS

		#1 Check if the form has been filled in correctly
		if form.is_valid():
			#2 If user sent the form, clean the data (username & password) sent from the form
			cd = form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])

			#3. If data is clean, then check if user exists
			if user is not None:
				#4 If user exits, check if user is active then user can login & send message
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated successfully')
				#5 If the authentication failed
				else:
					return HttpResponse('Disabled account')

			# IF USER NOT EXISTS

			#1 If user does not exist, send message
			else:
				return HttpResponse('Invalig login')

		# B. IF USER SENT GET REQUEST

	else:
		form = LoginForm()

	return render(request, 'account/login.html', {'form':form})	

