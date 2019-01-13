from django.shortcuts import render
# from django import forms
# from django.forms.utils import ErrorList
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet
from django.urls import reverse_lazy
from .forms import TweetModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create/'

    # def form_valid(self, form):
    #     if self.request.user.is_authenticated:
    #         form.instance.user = self.request.user
    #         return super(TweetCreateView, self).form_valid(form)
    #     else:
    #         form._errors[forms.forms.NON_FIELD_ERRORS]  = ErrorList(['user must be login to continue'])
    #         return self.form_invalid(form)
    # Fields = ['user', 'content']


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = '/tweet/'

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('home')

class TweetListView(ListView):
    template_name = 'tweets/list_view.html'
    queryset = Tweet.objects.all()

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/detail_view.html'

    # def get_object(self):
    #     return Tweet.objects.get(id=1)


# # Create your views here.
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     context = {
#         "object_list" : queryset
#     }
#     return render(request, "tweets/list_view.html", context)
#
# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)
#     context = {
#         "object" : obj
#     }
#     return render(request, "tweets/detail_view.html",context)
