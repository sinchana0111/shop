from django.urls import path
from . import views


urlpatterns=[path('register/',views.create_user,name='register'),
            path('login/',views.signin,name='login'),
            path('signout/',views.signout,name='signout'),          
            path('updatepwd/',views.update_password,name='updatepwd'),
            path('resetpwd/<str:username>/',views.reset_password,name='resetpwd'),
            path('identify/',views.IdentifyView,name='identify'),
            path('home/',views.home,name='home'),
            path('productlist/',views.product_list,name='productlist'),
            path('productdetails/<str:product_name>/',views.product_details_view,name='productdetails'),
            path('product/<int:id>/',views.productview,name='product'),
            path('product_view/<slug>/',views.products_view,name='product_view'),
            path('category/<slug>/', views.categoryView, name='category'),
            path('phome/',views.homeview,name='phome'),

]