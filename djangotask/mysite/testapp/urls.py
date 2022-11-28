from django.urls import path

from . import views

app_name='testapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('submit/', views.submit, name='submit'),
    path('remv/<int:lpk>', views.remv, name='remv'),
    path('edit/<int:lpk>', views.edit, name='edit'),
    path('editpage/<int:lpk>', views.editpage, name='editpage')
]