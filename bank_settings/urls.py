"""bank_settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers

from banking.views.account_viewset import AccountViewset
from banking.views.account_balance_viewset import AccountBalanceViewset
from banking.views.account_statement_viewset import AccountStatementViewset
from banking.views.transaction_viewset import TransactionViewset

router = routers.DefaultRouter()
router.register(r'account', AccountViewset)
router.register(r'transaction', TransactionViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('account/<int:pk>/balance/', AccountBalanceViewset.as_view()),
    path('account/<int:pk>/statement/',  AccountStatementViewset.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
