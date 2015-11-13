from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView 
from django.conf import settings
from django.conf.urls.static import static
from gallery.views import HomePage

urlpatterns = [
    # Examples:
    # url(r'^$', 'jessmathews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', TemplateView.as_view(
        template_name="gallery/contact.html"
    )),
    url(r'^$', HomePage.as_view()),
    #url(r'^$', TemplateView.as_view(
        #template_name="gallery/homepage.html"
    #)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
