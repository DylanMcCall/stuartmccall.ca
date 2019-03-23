from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class VisitorTrackingConfig(AppConfig):
    name = 'visitor_tracking'
    verbose_name = _("Visitor Tracking")
