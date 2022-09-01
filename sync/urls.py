from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from files.views import simple_upload


urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html"), name='home'),
    path("upload", simple_upload),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)