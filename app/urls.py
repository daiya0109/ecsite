from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'), # 追加
    path('product/<int:product_id>/', views.detail, name='detail'),
    path('fav_products/', views.fav_products, name='fav_products'),
    path('cart/', views.cart, name='cart'), # 追加
    path('change_item_amount/', views.change_item_amount, name='change_item_amount'), # 追加
    path('order_history/', views.order_history, name='order_history'),
    path('toggle_fav_product_status/', views.toggle_fav_product_status,
         name='toggle_fav_product_status'),
    path('login/',
         auth_views.LoginView.as_view(template_name='app/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]