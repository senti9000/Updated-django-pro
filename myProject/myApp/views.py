from django.shortcuts import render, redirect  
from .forms import RegisterForm
from .forms import FileUploadForm

# Create your views here.
def profile (request):
        return render(request,'profile.html')

def Login_Page(request):
        return render(request, 'Login_Page.html')

def register(request):
        if request.method =='POST':
                form = RegisterForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('Login_Page')
        else:
                form = RegisterForm()
                return render(request, 'register.html'('form',form))
        
def testPath (request):
        return render(request,'testPath.html')

def resume (request):
    return render(request, 'resume.html')
