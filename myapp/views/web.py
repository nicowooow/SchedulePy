from django.http import HttpResponse
from django.shortcuts import  render

def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Sitemap: https://schedulepy.nicowooow.site/sitemap.xml\n"
    )
    return HttpResponse(content, content_type="text/plain")

from django.http import HttpResponse

def simple_sitemap(request):
    urls = [
        "https://schedulepy.nicowooow.site/",
        "https://schedulepy.nicowooow.site/about/",
        "https://schedulepy.nicowooow.site/schedule/",
    ]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        xml.append(f"  <url><loc>{u}</loc></url>")
    xml.append("</urlset>")
    return HttpResponse("\n".join(xml), content_type="application/xml")

def custom_404(request, exception):
    return render(request, "404.html",{ "page_css":"css/custom404.css"}, status=404)