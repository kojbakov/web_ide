from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tests_list, name='tests_list'),
    url(r'^test/(?P<pk>\d+)/$', views.test_detail, name='test_detail'),
    url(r'^test/new/$', views.new_test_case, name='new_test_case'),
    url(r'^test/(?P<pk>\d+)/edit/$', views.test_edit, name='test_edit'),
    url(r'^test/(?P<pk>\d+)/delete/$', views.test_delete, name='test_delete'),
]