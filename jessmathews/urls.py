from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView 
#from photologue.sitemaps import GallerySitemap, PhotoSitemap

#sitemaps = {
    #'photologue_galleries': GallerySitemap,
    #'photologue_photos': PhotoSitemap,
#}

urlpatterns = [
    # Examples:
    # url(r'^$', 'jessmathews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^$', TemplateView.as_view(
        template_name="gallery/homepage.html"
    ))
]
