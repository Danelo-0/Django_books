from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Index, name='Index'),
    path('books/', views.AllBook, name='AllBook'),
    path('author/', views.AllAuthor, name='AllAuthor'),
    path('book/<int:id>/', views.OneBook, name='OneBook'),
    path('author/<int:id>/', views.OneAuthor, name='OneAuthor'),
    path('add/', views.AddShow, name='AddShow'),
    path('book/<int:id>/delete', views.Delete, name='Delete'),
    path('register/', views.RegisterUser, name='Register'),
    path('logout/', views.Logout, name='Logout'),
    path('login/', views.Login, name='Login'),
    path('profile/', views.ProfileShow, name='Profile'),
    path('profile/update/', views.ProfileUpdateView, name='Update'),
    path('profile/updatePassword', views.ProfileUpdatePassword, name='UpdatePassword')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
