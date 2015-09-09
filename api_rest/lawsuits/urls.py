from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from lawsuits import views

urlpatterns = [
    url(r'^lawsuits/$', views.LawsuitList.as_view()),
    url(r'^lawsuits/(?P<pk>[0-9]+)/$', views.LawsuitDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)