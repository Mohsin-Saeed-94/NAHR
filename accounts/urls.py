from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),
    path('courses/', views.coursesPage, name="courses"),
    path('', views.home, name="home")
    #path('products/', views.products, name='products'),
   # path('customer/<str:pk_test>/', views.customer, name="customer"),

]