from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


from boot.models import Inquiry

# Create your views here.
def test(request):
    return render(request, 'base.html')



def blog(request):
    if not request.user.is_authenticated:
        return redirect('boot:login')
    return render(request, 'boot/blog.html')

def about(request):
    return render(request, 'boot/about.html')

def contact(request):
    return render(request, 'boot/contact.html')


def index(request):
    print(request.user.is_authenticated)
    return render(request, 'boot/index.html')




def post_contact(request):
     if request.method =='GET':
         return redirect('boot:contact')
    
     elif request.method == 'POST':
        new_post = Inquiry()
        new_post.fullname = request.POST['fullname']
        new_post.email = request.POST['email']
        new_post.phone_number = request.POST['phone_number']
        new_post.message = request.POST['message']

        new_post.save()

        return redirect('boot:contact')

def login(request):
    if request.user.is_authenticated:
        return redirect('boot:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(
            request, 
            username = username,
            password = password
            )
        if user is not None:
            auth.login(request, user)
            return redirect('boot:index')
        
    return render(request, 'boot/login.html')

def sign_up(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_check = request.POST.get('password_check')
       

        if username is not None and password is not None and password == password_check :
            new_user =User.objects.create_user(
                username = username,
                password = password,
                )
            return redirect('boot:index')
        
    return render(request, 'boot/sign_up.html')

def logout(request):
    print(request.user.is_authenticated)
    if request.method =='POST':
        auth.logout(request)
    
    return redirect('boot:index')