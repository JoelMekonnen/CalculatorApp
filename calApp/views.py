from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View, UpdateView
from django.contrib.auth.models import User 
from .forms import CustomUserCreationForm, ResultForm
from .models import ResultHistory
from django.http import HttpResponse
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
# Create your views here.

def homepage(request):
    #this function defines the homepage view 
    return render(request, template_name='index.html')

class HistoryPage(View):
    #here we defin the get and post methods and override them
    form_class = ResultForm
    template_name = 'index.html'
    def get(self,request):
        form = ResultForm
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = ResultForm(request.POST) 
        res = ResultHistory()
              #Cleaned (normalized data)
        res.user = request.user
        res.expression = request.POST.get("expression")
        res.result = request.POST.get("result")
        print(request.POST)
        res.save(self)
        return redirect('save')

class ShowHistory(View):
    model = ResultHistory
    template_name = "history.html"
    def get(self, request):
        history = ResultHistory.objects.filter(user=self.request.user)
        return render(request, self.template_name, {'result': history})

class userUpdate(UpdateView):
    model = User
    template_name = "update.html"
    success_url = reverse_lazy('save')
    fields = ['username', 'first_name', 'last_name',]

        
