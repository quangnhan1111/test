from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # path('companies/', views.CompanyMixins.as_view(), name='list_company'),
    # path('company/<int:pk>/', views.DetailCompanyMixins.as_view(), name='list_company'),
    path('company-test', views.get_list, name='test')
]
