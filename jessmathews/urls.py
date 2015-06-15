from django.conf.urls import include, url
from django.contrib import admin
from gallery.views import HomePageView

urlpatterns = [
    # Examples:
    # url(r'^$', 'jessmathews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view()),
]
