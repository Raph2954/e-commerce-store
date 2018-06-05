from untitled13.catalog.models import Category
from untitled13 import settings


def untitled13(request):
    return {
        'active_categories': Category.objects.filter(is_active = True),
        'site_name': settings.SITE_NAME,
        'meta_keywords': settings.META_KEYWORDS,
        'meta_description': settings.META_DESCRIPTION,
        'request': request
    }