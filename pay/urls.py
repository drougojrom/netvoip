from django.urls import path, re_path
from django.views.generic.base import TemplateView
from pay.views import AccountList, AccountDetail, LoginView, LogoutView, Balance_Add, Cost, SupplierGet, Cdrs_for_Page, CdrExportView

urlpatterns = [
    path('account/', AccountList.as_view(), name='accountactions'),
    path('account/<int:id>/', AccountDetail.as_view(), name='accountactionsdetail'),
    path('account/<int:id>/<str:tenant>/', Balance_Add.as_view(), name='balance_add'),
    re_path(r'^$',LoginView.as_view(),name='index'),
    path('dashboard/<int:page>/', Cdrs_for_Page.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('cost', Cost.as_view(), name='cost'),
    path('supplierquery',SupplierGet.as_view(), name='supplierquery'),
    path('cdrexportzip/<str:tenant>/<str:account>/<str:timestart>/', CdrExportView.as_view(), name='cdrexportzip')
]