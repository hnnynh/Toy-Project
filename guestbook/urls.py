from django.urls import path
from guestbook.views import *

urlpatterns = [
    path('', post_operation, name = 'get_all_posts'),
    path('delete/<int:id>/', delete_post, name = 'delete_post'),
]