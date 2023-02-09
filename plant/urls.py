from django.urls import path
from django.conf.urls import url
from.import views
urlpatterns = [
    path('',views.base, name='base'),
    path('/test',views.test, name='test'),
    path('/set_date',views.set_date,name='set_date'),
    path('/create_plant', views.PlantAddView.as_view(), name='create_plant'),
    path('/update/<int:pk>', views.PlantUpdateView.as_view(), name='update_plant'),
    path('/delete/<int:pk>', views.PlantDeleteView.as_view(), name='delete_plant'),


    
]


