from django.shortcuts import render, redirect
from config.forms import NameForm
from config.models import Person
# Create your views here.
def index_view(request):
    return render(request, "index.html")
def contacts_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            name=request.POST['name']
            email=request.POST['email']
            phone=request.POST['phone']
            contact=Person.objects.create(name=name,email=email,phone=phone)
            # redirect to a new URL:
            return redirect('/index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "Contacts.html", {'form': form})
def rdrct(request) :
    return redirect('/index.html')