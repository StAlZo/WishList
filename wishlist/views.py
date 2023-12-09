from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView, ListView

from wishlist.forms import AddWishList, AddGoods, CreateWishList
from wishlist.models import WishList


def index(requerst):
    #return HttpResponse("wishlist")
    return render(requerst, 'MainPage.html')


def login(requerst):
    return render(requerst, 'login.html')


class CreateList(CreateView):
    #model = WishList
    form_class = AddWishList
    template_name = 'create_list.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(CreateList, self).get_context_data(**kwargs)
        context['wishlist'] = AddWishList
        context['goods'] = AddGoods
        return context

    def form_valid(self, form):
        article = form.save(commit=False)
        article.owner_user_id = self.request.user
        #article.save()  # This is redundant, see comments.
        return super(CreateList, self).form_valid(form)


class ViewList(ListView):
    model = WishList
    template_name = 'list.html'
