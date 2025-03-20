from django.shortcuts import render
from .forms import GetUser
from .models import UserHistory
# Create your views here.

def history_dashboard(request):
	user_history = None
	message = ""
	if request.method == 'POST':
		form = GetUser(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']

			user_history = UserHistory.objects.filter(user = username).order_by('-id')
			if user_history.exists():
				return render(request, 'history/history.html',{
					'username': username,
					'form': form,
					'user': user_history,
					'showPopup':False,
					'show_history': True
				})

			if not user_history.exists():
				form = GetUser()
				message = 'User does not exists'
	else:
		form = GetUser()

	return render(request, 'history/history.html',{
		'form': form,
		'showPopup':True,
		'show_history': False,
		'message': message
	})
