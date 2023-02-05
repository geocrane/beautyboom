from django.conf.urls import url

from . import views

app_name = "shop"

urlpatterns = ([url(r'^$', views.index, name='index'),
                url(r'^(?P<category_slug>[-\w]+)/$', views.product_list,
                    name='category'),
                url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail,
                    name='product_detail'), ])
