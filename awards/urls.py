from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url(r'^$',views.awards_day,name='awardsToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^projects/(\d+)',views.projects,name ='projects'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_awards,name = 'pastAwards')    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)