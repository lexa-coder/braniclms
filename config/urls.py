from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', views.ContactsView.as_view()),
    path('courses/', views.CursesListView.as_view()),
    path('doc_site/', views.DocSiteView.as_view()),
    path('', views.IndexView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('news/', views.NewsView.as_view()),

]
