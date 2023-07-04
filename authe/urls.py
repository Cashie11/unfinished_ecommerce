from django import urls
from authe import views


urlpatterns = [
    urls.path('signup', views.signup, name='signup'),
    urls.path('login', views.handlelogin, name='login'),
    urls.path('logout', views.handlelogout, name='logout'),
    urls.path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(), name='activate'),
    urls.path('request-reset-email/',views.RequestResetEmailView.as_view(),name='request-reset-email'),
    urls.path('set-new-password/<uidb64>/<token>',views.SetNewPasswordView.as_view(),name='set-new-password'),
]
