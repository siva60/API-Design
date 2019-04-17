from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    # put the decorator on the get() or post() methods. Or Put on the entire View itself.
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)  # =super(CSRFExemptMixin, self)

