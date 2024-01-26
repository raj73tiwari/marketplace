
from django.urls import path
from .import views

app_name="basicapp"
urlpatterns = [
    path('', views.index , name='index'),
    path('myprods/', views.my_prods , name='myprods'),
    path('owner/<int:id>/', views.owner , name='owner-info' ),
    path('add-prod/', views.add_prod , name='add-prod' ),
    path('update-prod/<int:prod_id>/', views.update_prod , name='update-prod' ),
    path('del-prod/<int:prod_id>/', views.del_prod , name='del-prod' ),
]