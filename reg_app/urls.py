from django.urls import include, path
from rest_framework import routers
from django.urls import path
from . import views
from .views import MainDataViewset,HeroViewSet

router = routers.DefaultRouter()
router.register(r'Publish', views.HeroViewSet)
router.register(r'Userdata', views.MainDataViewset)

urlpatterns=[
    path('index',views.index,name='index'),
    path('add',views.add,name='add'),
    #path('post',views.display,name='post'),
    #path('ad',views.admin,name='ad'),
    #path('add_img',views.image,name='add_img'),
    path('dis/<tittle>//<contend>/',views.dis,name='dis'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
