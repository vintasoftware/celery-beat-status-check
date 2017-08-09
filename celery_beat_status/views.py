from django.views.generic import TemplateView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.utils.text import ugettext_lazy as _
from celery_beat_status.helpers import get_periodic_tasks_info


class PeriodicTasksStatusListView(TemplateView):
    template_name = "celery_beat_status/periodic_tasks_status_list.html"
    site_url = "/"

    @method_decorator(user_passes_test(
        lambda u: u.is_staff and u.is_superuser,
        login_url='admin:login'
    ))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Periodic tasks status')
        context['user'] = self.request.user
        context['site_url'] = self.site_url
        context['has_permission'] = self.request.user.is_superuser
        context['tasks'] = get_periodic_tasks_info()

        return context