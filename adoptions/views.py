from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'pets':pets,
    })
    #return HttpResponse('<p>Home View</p>')

def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExists:
        raise Http404('Pet Not Found')

    return render(request,'pet_detail.html',{
        'pet':pet,
    })
        

    #return HttpResponse(f'<p>Pet Detail View with arg as {pet_id}</p>')

    