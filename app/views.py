from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
     background=Post.objects.get(category_id=1)
     blog=Post.objects.get(category_id=2)
     blog1=Post.objects.filter(category_id=7)
     hero=Post.objects.get(category_id=8)
     features=Post.objects.filter(category_id=5)
     about=Post.objects.get(category_id=4)
     deal=Post.objects.get(category_id=9)
     Features=Post.objects.get(category_id=10)
     Features1=Post.objects.filter(category_id=11)
     Features2=Post.objects.get(category_id=12)
     Features3=Post.objects.filter(category_id=13)
     how=Post.objects.get(category_id=14)
     how1=Post.objects.filter(category_id=15)
     product=Post.objects.get(category_id=3)
     product1=Post.objects.filter(category_id=16)
     testmonial=Post.objects.get(category_id=6)
     testmonial1=Post.objects.filter(category_id=17)
     newsletter=Post.objects.get(category_id=18)




     data={
        'background':background,
        'blog':blog,
        'blog1':blog1,
        'hero':hero,
        'features':features,
        'about':about,
        'deal':deal,
        'Features':Features,
        'Features1':Features1,
        'Features2':Features2,
        'Features3':Features3,
        'how':how,
        'how1':how1,
        'product':product,
        'product1':product1,
        'testmonial':testmonial,
        'testmonial1':testmonial1,
        'newsletter':newsletter,
     }
     return render(request,"index.html",data)


def about(request):
     about=Post.objects.get(category_id=4)
     about1=Post.objects.get(category_id=19)
     features=Post.objects.filter(category_id=5)
     newsletter=Post.objects.get(category_id=18)


     data={
          'about1':about1,
          'about':about,
          'features':features,
          'newsletter':newsletter,

     }
     return render(request,"about.html",data)


def product(request):
     product2=Post.objects.get(category_id=20)
     product=Post.objects.get(category_id=3)
     product1=Post.objects.filter(category_id=16)
     newsletter=Post.objects.get(category_id=18)
     

     data={
          'product2':product2,
          'product':product,
          'product1':product1,
          'newsletter':newsletter,

     }
     return render(request,"product.html",data)


def feature(request):

     Features4=Post.objects.get(category_id=21)
     features=Post.objects.filter(category_id=5)
     Features=Post.objects.get(category_id=10)
     Features1=Post.objects.filter(category_id=11)
     Features2=Post.objects.get(category_id=12)
     Features3=Post.objects.filter(category_id=13)
     newsletter=Post.objects.get(category_id=18)

     data={
          'Features4':Features4,
          'features':features,
          'Features':Features,
          'Features1':Features1,
          'Features2':Features2,
          'Features3':Features3,
          'newsletter':newsletter,

     }
     return render(request,"feature.html",data)



def howtouse(request):
     how2=Post.objects.get(category_id=22)
     features=Post.objects.filter(category_id=5)
     how=Post.objects.get(category_id=14)
     how1=Post.objects.filter(category_id=15)

     data={
          'how2':how2,
          'features':features,
          'how':how,
          'how1':how1,
     }
     return render(request,"how-to-use.html",data)

def testimonial(request):
     testmonial2=Post.objects.get(category_id=23)
     features=Post.objects.filter(category_id=5)
     testmonial=Post.objects.get(category_id=6)
     testmonial1=Post.objects.filter(category_id=17)

     data={
          'testmonial2':testmonial2,
          'features':features,
          'testmonial':testmonial,
          'testmonial1':testmonial1,

     }
     return render(request,"testimonial.html",data)



def blog(request):
     blog2=Post.objects.get(category_id=24)
     blog=Post.objects.get(category_id=2)
     blog1=Post.objects.filter(category_id=7)
     newsletter=Post.objects.get(category_id=18)

     data={
        'blog':blog,
        'blog1':blog1,
        'blog2':blog2,
        'newsletter':newsletter,
     }
     return render(request,"blog.html",data)



def error(request):
     error=Post.objects.get(category_id=25)
     newsletter=Post.objects.get(category_id=18)
     error1=Post.objects.get(category_id=26)

     data={
          'error':error,
          'newsletter':newsletter,
          'error1':error1,
     }

     return render(request,"404.html",data)


def contact(request):
     contact=Post.objects.get(category_id=27)
     newsletter=Post.objects.get(category_id=18)
     contact1=Post.objects.filter(category_id=28)
     contact2=Post.objects.get(category_id=29)


     data={
          'contact':contact,
          'newsletter':newsletter,
          'contact1':contact1,
          'contact2':contact2,

     }
     return render(request,"contact.html",data)