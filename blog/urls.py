from django.urls import path,re_path
from . import views
app_name = 'blog'
urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^delete/(?P<inputId>[0-9]+)/$',views.delete,name='delete'),
    re_path(r'^tambah/form',views.getFormCreate,name='formTambah'),
    re_path(r'^update/form/(?P<inputId>[0-9]+)/$',views.updataPost,name='update'),
]