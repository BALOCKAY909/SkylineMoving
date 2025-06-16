"""
URL configuration for skyline_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.views.generic import TemplateView
import os

def robots_txt(request):
    content = """User-agent: *
Allow: /

# Sitemap location
Sitemap: https://skylinemovinggp.com/sitemap.xml

# Block access to admin and other sensitive areas
Disallow: /admin/
Disallow: /*.pyc$
Disallow: /static/admin/"""
    return HttpResponse(content, content_type="text/plain")

def sitemap_xml(request):
    content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://skyline-moving-gp-9286c2aaa5d9.herokuapp.com/</loc>
        <lastmod>2025-06-15</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>"""
    return HttpResponse(content, content_type="application/xml")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quotes.urls')),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap_xml, name='sitemap_xml'),
]
