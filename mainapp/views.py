from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
class ContactsView(TemplateView):
    template_name = 'contacts.html'


class CursesListView(TemplateView):
    template_name = 'courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'doc_site.html'


# class IndexView(TemplateView):
#     template_name = 'index.html'


def index(requset):
    return render(requset, 'index.html')


class LoginView(TemplateView):
    template_name = 'login.html'


class NewsView(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Новость раз'
        context_data['preview'] = 'Превью к новости раз'
        context_data['date'] = '2022-01-01'
        return context_data
