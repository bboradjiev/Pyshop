from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import (TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy, reverse
from . import forms, models

from .forms import PostProduct


class IndexView(TemplateView):
    template_name = 'index.html'


class ProductListView(ListView):
    context_object_name = 'products'
    models = models.Product

    def get_queryset(self):
        return models.Product.objects.order_by('id')


class ProductDetailView(LoginRequiredMixin, DetailView):
    login_url = '/products/user_login/'
    redirect_field_name = 'products/product_detail_page.html'
    context_object_name = 'product_detail'
    model = models.Product
    template_name = 'products/product_detail_page.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = '/products/user_login/'
    fields = ('name', 'price', 'stock', 'image_url')
    model = models.Product


class ProductUpdateView(UpdateView):
    fields = ('name', 'price', 'stock', 'image_url')
    models = models.Product

    def get_queryset(self):
        return models.Product.objects.order_by('id')


class ProductDeleteView( DeleteView):

    model = models.Product
    success_url = reverse_lazy('product:list')


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

        registered = True

    else:
        user_form = UserForm()

    return render(request, 'registration.html',
                  {'user_form': user_form,
                   'registered': registered})


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                print("logged it")
                return render(request, 'index.html')
            else:
                return HttpResponse('account not active')
        else:
            print("someone tried to log")
            return render(request, 'products/login.html')
    else:
        return render(request, 'products/login.html')


@login_required
def user_logout(request):
    logout(request)
    print('logged out')
    return render(request, 'index.html')