from django.shortcuts import render
from .models import Tweet
from .forms import TweetModelForm
from django.views.generic import ListView, DetailView, CreateView


class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/forms.html'
    Fields = ['user', 'content']

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
