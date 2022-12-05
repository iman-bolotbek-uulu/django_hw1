from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/detail/',views.detail,name='detail'),
    path('<int:id>/result/',views.result,name='result'),
    path('<int:id>/vote/',views.vote,name='vote'),
    path('shop/',views.item,name='item'),
    path('detail_item/<int:id>',views.detail_item,name='detail_item'),
]
