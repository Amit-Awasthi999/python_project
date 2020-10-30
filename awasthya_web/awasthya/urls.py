from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('createuser', views.createuser, name="createuser"),
    path('login', views.login, name="login"),
    path('catlog.html', views.catlog, name="catlog")

]