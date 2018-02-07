from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^list$', views.post_list),
    url(r'^create/$', views.post_create),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)