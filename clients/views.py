from django.http import Http404
from django.shortcuts import render
from .models import Client, Expense

# Create your views here.
def client_list(request):
	all_clients_list = Client.objects.all()
	return render(request, 'client_list.html', {'clients_list': all_clients_list})


def client_detail(request, client_id):
	try:
		get_details = Client.objects.get(id=client_id)
	except Client.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'client_detail.html', {'clients_detail': get_details})
