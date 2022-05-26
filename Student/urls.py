from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', loggedout, name='loggedout'),
    path('subjects/', subjects, name='subjects'),
    path('add-subject/' , add_subject),
    path('delete_subject/<int:id>', delete_subject, name='delete_subject'),
    path('edit_subject/<int:id>', edit_subject, name='edit_subject'),
]