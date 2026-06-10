from django.urls import path
#import  کردن تابعنی که در ویو بود
from  website.views import *


urlpatterns = [
    # path ('urls address' , 'view')
    path('index' , index_view),
    path('about' , about_view),
    path('contact' , contact_view),
]