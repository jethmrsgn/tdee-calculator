from django.urls import path
from . import views

urlpatterns = [
	path('dashboard/', views.history_dashboard, name='history-dashboard'),

]
