from django.shortcuts import render
from .models import LeaveMessage
# Create your views here.

def index(request):
	context = {
	
	}
	return render(request, 'index.html', context=context)