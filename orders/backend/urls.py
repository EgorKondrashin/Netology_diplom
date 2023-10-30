from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterAccount, ConfirmAccount, ContactView, LoginAccount, ShopView, CategoryView, \
    ProductInfoView, PartnerUpdate, PartnerState, PartnerOrders, AccountDetails, BasketView, OrderView

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('shops', ShopView)
router.register('categories', CategoryView)
router.register('products', ProductInfoView, basename='products')

urlpatterns = [
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),
]

urlpatterns.extend(router.urls)
