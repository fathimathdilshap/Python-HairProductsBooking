from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('error',views.error,name='error'),
    path('blog',views.blog,name='blog'),
    path('product',views.product,name='product'),
    path('howtouse',views.howtouse,name='howtouse'),
    path('feature',views.feature,name='feature'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('contact',views.contact,name='contact'),
]