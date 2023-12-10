from django.http import Http404


class DjangoUtils(object):

    @classmethod
    def fetch_object_or_404(cls, clz, msg: str = None, format:bool = False, **kwargs):
        try:
            return clz.objects.filter(**kwargs)
        except Exception as e:
            raise (Http404(msg.format(e)) if format else Http404(msg))
