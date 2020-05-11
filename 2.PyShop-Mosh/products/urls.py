from django.urls import path
from . import views, forms

app_name = 'product'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('list/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('list/', views.ProductListView.as_view(), name='list'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),
    path('user_login/', views.user_login, name='user_login'),
    # path('user_logout/', views.user_logout, name='user_logout'),

]