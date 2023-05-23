from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('courses/', views.CursesListView.as_view(), name='courses'),
    path('doc_site/', views.DocSiteView.as_view(), name='doc_site'),
    path('', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('news/', views.NewsView.as_view(), name='news'),

]
