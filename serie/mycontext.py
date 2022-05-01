from .models import Serie


def recent (request):
    date = Serie.objects.all().order_by('-date')[0:5]
    return {"recent": date}


def trending (request):
    views = Serie.objects.all().order_by('-views')[0:5]
    return {"trending": views}
