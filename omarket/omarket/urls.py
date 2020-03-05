"""omarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings #esto se importa para la media
from django.conf.urls.static import static #esto se importa para la media
from products import views as product_views
from users import views as user_views

from omarket import Gviews

urlpatterns = [
    path('home/', Gviews.Home, name="home"),
    path('compras/', Gviews.Compras, name="compras"),
    path('admin/', admin.site.urls),

    path('crud-productos/', product_views.crudProduct, name="crud-productos"),
    path('product-list/', product_views.productList, name="product-list"),
    path('product-list/<int:id>/', product_views.crudProduct, name="product-update"),

    path('crud-piece/', product_views.crudPiece, name="crud-piece"),
    path('piece-list/', product_views.pieceList, name="piece-list"),
    path('piece-list/<int:id>/', product_views.crudPiece, name="piece-update"),

    path('crud-animal/', product_views.crudAnimal, name="crud-animal"),
    path('animal-list/', product_views.animalList, name="animal-list"),
    path('animal-list/<int:id>/', product_views.crudAnimal, name="animal-update"),

    path('crud-corte/', product_views.crudCorte, name="crud-corte"),
    path('corte-list/', product_views.corteList, name="corte-list"),
    path('corte-list/<int:id>/', product_views.crudCorte, name="corte-update"),

    path('asignar-precio/', product_views.asignarPrecio, name="asignar-precio"),
    path('precios-list/', product_views.precioList, name="precios-list"),
    path('precios-list/<int:id>/', product_views.asignarPrecio, name="precio-update"),

    #path('delete-product'),
    path('users/login', user_views.login_view, name="login"),
    path('users/logout', user_views.logout_view,name='logout'),
    path('users/signup',user_views.signup,name="signup")

] 
#+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
