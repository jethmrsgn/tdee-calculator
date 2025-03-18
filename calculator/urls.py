from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('result/',views.result, name='result'),
	path('result/<str:plan>/<int:current_tdee>',views.result, name='result-plan')
]
