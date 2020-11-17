from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .forms import PersonForm
from .models import Person

# Create your views here.
def home( request):
    return render ( request, 'myapp/home.html')

def person( request):
    if request.method=="GET":
        personForm = PersonForm()
        context = {'personForm': personForm}
        return render ( request, 'myapp/person.html', context)
    elif request.method=="POST":
        personForm = PersonForm( request.POST)
        if personForm.is_valid() == False:
            return HttpResponse(personForm.errors)
        personForm.save()
        return redirect("http://localhost:8000/persons")

def updateperson( request, id=None):
    if request.method=="GET":
        person = get_object_or_404(Person, id=id)       #setting the id to id of whatever Person
        personForm = PersonForm(instance=person)
        context = {'personForm': personForm}
        return render ( request, 'myapp/updateperson.html', context)
    elif request.method=="POST":
        personForm = PersonForm( request.POST)
        if personForm.is_valid() == False:
            return HttpResponse(personForm.errors)
        personForm.save()
        return redirect("http://localhost:8000/persons")

def deleteperson( request, id):
    if request.method=="GET":
        person = get_object_or_404(Person, id=id)       #setting the id to id of whatever Person
        person.delete()
        return redirect("http://localhost:8000/persons")

def persons( request):
    persons = Person.objects.all()
    context = {'persons': persons}
    request render( request, 'myapp/persons.html', context)

def getTotal( request):
    print('inside getTotal')
    persons = Person.objects.all()
    total = 0
    for person in persons:
        total = total+int(person.age)
    print('total='+str(total))
    return JSonResponse({'total': total})     #passes through Json response
