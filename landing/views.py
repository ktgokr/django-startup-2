import random
import django
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from landing.models import Post


def index(request):
    return render(request, "index.html")



def post_create(request):
    if request.method =='GET':
         return render(request, "landing/create.html")
    elif request.method =='POST':
        # new_post = Post()
        # new_post.title = request.POST['title']
        # new_post.content = request.POST['content']
        # new_post.save()
        # return HttpResponseRedirect(reverse('landing:read_all'))
        print(request.POST['title'])
        print(request.POST['content'])
        # print(request.POST["image"])
        if request.POST['image']:
            print(request.FILES['image'])
            
        new_post = Post()
        new_post.title = request.POST['title']
        new_post.content = request.POST['content']
        if request.FILES.get("image"):
            new_post.head_image = request.FILES['image']

        new_post.save()
        return redirect('landing:read_all')

def post_read_all(request):
    post_list = Post.objects.all()
    context = {
        'posts' : post_list
    }
    return render(request, 'landing/read-all.html', context)


def post_read(request, post_id):

    post = Post.objects.get(id = post_id)

    context = {
        'post' : post,
        'writer' : post.writer
    }
    return render(request, 'landing/read.html', context)


def post_update(request, post_id):
    if request.method =='GET':
         
        post =Post.objects.get(id = post_id)
        context = {
            'post' : post
        }
        return render(request, "landing/update.html", context)
    
    
    elif request.method =='POST':
        target_post = Post.objects.get(id = post_id)
        target_post.title = request.POST['title']
        target_post.content = request.POST['content']
        target_post.save()
        
        return HttpResponseRedirect('/landing/read-all/')


def post_delete(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id = post_id)
        context = {
            'post' : post
        }
        return render(request, 'landing/delete.html', context)
    elif request.method == 'POST':
        delete_post = Post.objects.get(id = post_id)
        delete_post.delete()
        return HttpResponseRedirect('/landing/read-all/')


def temp_test(request):

    context = {
        # 'weather' : '맑음',
        'temperature' : 5,
        'weather' :{
            'weather' : '맑음',
            'temperature' : 15
        },
        'player' : [{
                        'name': '손흥민',
                        'team' : '토트넘'
                    },
                    {
                        'name': '메시',
                        'team' : '파이생제르'
                    },
                    {
                        'name': '차범근',
                        'team' : '레버쿠젠'
                    }]
    }
    return render(request, 'landing/temptest.html', context)

# def login(request):
#         if request.method == 'GET':
#             id = request.args.get('id')
#             pw = request.args.get('pw')

#         elif request.method == 'POST':
#             print('POST Method')
#             id = request.form['id']
#             pw = request.form['pw']

#         return HttpResponseRedirect('/landing/read-all/')

