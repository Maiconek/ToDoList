from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.urls import reverse_lazy

# Create your views here.
def create(request):
    task = Task.objects.all()
    
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('Task was successfully created')
        return redirect('/')
    context = {'tasks': task, 'form': form}
    return render(request, "base.html", context)


def update(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            print('Updated')
        return redirect('/')
    context = {'form' : form}
    return render(request, "update.html", context)

def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("/")
    

class CustomLoginView(LoginView):
    template_name = "login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home")
        return super(RegisterPage, self).get(*args, **kwargs)
    
    

