from django.urls import path
from . import views
from .views import PostList, EntryView, AddPost, EditPost, DeletePost

urlpatterns = [
    #path('', HomeView.as_view(), name='home'),
    path('', views.homeView, name='home'),
    path('acerca/', views.acercaView, name='acerca'),
    path('acciones/', views.accionesView, name='acciones'),
    path('contacto/', views.contactoView, name='contacto'),
    path('blog/', PostList.as_view(), name='blog'), 
    path('blog/entry/<int:pk>', EntryView.as_view(), name='entry'),
    path('blog/add_post/', AddPost.as_view() , name='add_post'),
    path('blog/entry/<int:pk>/edit_post/', EditPost.as_view() , name='edit_post'),
    path('blog/entry/<int:pk>/delete_post/', DeletePost.as_view() , name='delete_post'),
]