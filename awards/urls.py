from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url(r'^$',views.awards_day,name='awardsToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^projects/(\d+)',views.projects,name ='projects'),
    url('project/(\d+)', views.projects, name='project_results'),
    url(r'^new/projects$', views.new_projects, name='new_projects'),
    url(r'^new/profile$', views.new_profile, name='new-profile'),
    url(r'^api/merch/$', views.MerchList.as_view()),
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',
    views.MerchDescription.as_view()),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_awards,name = 'pastAwards'),
    url(r'ratings/', include('star_ratings.urls', namespace='ratings')),    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)