from django.urls import path

from boot import views

app_name='boot'
urlpatterns =[
    path('base/', views.test),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('inquiry/contact/', views.post_contact, name='inquiry/contact'),
    path('login/', views.login, name='login'),
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('logout/', views.logout, name = 'logout'),

]