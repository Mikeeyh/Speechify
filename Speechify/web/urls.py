from django.urls import path
from Speechify.web.views import index


from . import views

urlpatterns = (
    path("", index, name="index"),

    # adding:
    path('download/<path:path>/', views.download, name='download'),
)
