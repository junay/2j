# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    (r'^$', 'list_contents'),
    (r'^create/$', 'add_content'),
    (r'^show/(?P<key>.+)$', 'show_content'),
    (r'^edit/(?P<key>.+)$', 'edit_content'),
    (r'^delete/(?P<key>.+)$', 'delete_content'),
    (r'^append/(?P<key>.+)$', 'append_comment'),
)
