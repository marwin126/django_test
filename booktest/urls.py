#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from django.conf.urls import url
from booktest import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^books$',views.books),
    url(r'^books/(\d+)$',views.detail),
    #url(r'^(\d+)$',views.detail),
]