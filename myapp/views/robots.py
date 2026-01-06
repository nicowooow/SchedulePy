from django.http import HttpResponse

def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Sitemap: https://schedulepy.nicowooow.site/sitemap.xml\n"
    )
    return HttpResponse(content, content_type="text/plain")
