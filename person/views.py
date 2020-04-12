from django.shortcuts import render,HttpResponse,redirect
from person.form import PersonForm
from .models import person


# Create your views here.
def Person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('show')
            except Exception as e:
                return HttpResponse("<h1> {error} </h1>".format(error=e.args[0]))
    else:
        form = PersonForm()
    return render(request,'person/index.html',{'form':form})

def show(request):
    persons = person.objects.all()
    return render(request,'person/show.html',{'person':persons})   

def edit(request,id):
    p = person.objects.get(id=id) 
    return render(request,'person/edit.html',{'person':p})

def update(request,id):
    p = person.objects.get(id=id)
    form = PersonForm(request.POST,instance=person)
    if form.is_valid():
        return redirect('person/show.html')
    return render(request,'person/edit.html',{'person':p})

def delete(request,id):
    p = person.objects.get(id=id)
    p.delete()
    return render('person/show.html')
            


# def show(request):
#     return render(request,'person/show.html')

# def add(request):
#     return render(request,'person/add.html')

# def login(request):
#     username = "not logged in"
#     if request.method == "POST":
#         MyLoginForm = form(request.POST)
    
#         if MyLoginForm.is_valid():
#             username = MyLoginForm.cleaned_data['username']
#     else:   
#         MyLoginForm = form()
#     return render(request,'person/login.html')    

# def edit(request):
#     return 

# def delete(request):
#     return            