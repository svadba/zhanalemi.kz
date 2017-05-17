from django.views import generic
from .models import Photo, Album



class IndexView(generic.ListView):
    template_name = 'albome/index.html'
    context_object_name = 'photoss'
    model = Photo

    def get_queryset(self):
        photos = Photo.objects.all()
        return split_categories(photos)


def split_categories(ps):
    b = int(len(ps) / 4)
    c = 0
    d = 0
    ress = []
    while b >= 0 and d < 2:
        ress.append(ps[c:(c + 4)])
        b -= 1
        c += 4
        d += 1
    return ress


def split_subcategories(qs):
    b = int(len(qs) / 8)
    c = 0
    res = []
    while b >= 0:
        res.append(qs[c:(c + 8)])
        b -= 1
        c += 8
    return res


class ProView(generic.ListView):
    template_name = 'albome/detail.html'
    context_object_name = 'photos'
    model = Photo

    def get_queryset(self):
        photos = Photo.objects.all()
        if self.kwargs.get('album'):
            album_filter = Album.objects.get(slug=self.kwargs['album'])
            photos = photos.filter(album=album_filter)
        return split_subcategories(photos)


