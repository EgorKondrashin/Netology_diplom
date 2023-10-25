from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterAccount, ConfirmAccount, ContactView, LoginAccount

router = DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
]

urlpatterns.extend(router.urls)
