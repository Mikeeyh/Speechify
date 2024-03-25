from django.urls import path

from Speechify.accounts.views import SignInUserView, SignUpUserView, signout_user

urlpatterns = (
    path("signin/", SignInUserView.as_view(), name="signin user"),
    path('signup/', SignUpUserView.as_view(), name='signup user'),
    path("signout/", signout_user, name="signout user"),
)
