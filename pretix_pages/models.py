from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from pretix.base.i18n import I18nCharField, I18nTextField
from pretix.base.models import LoggedModel


class Page(LoggedModel):
    event = models.ForeignKey('pretixbase.Event')
    slug = models.CharField(
        max_length=150, db_index=True, verbose_name=_('URL form'),
        validators=[
            RegexValidator(
                regex="^[a-zA-Z0-9.-]+$",
                message=_("The slug may only contain letters, numbers, dots and dashes.")
            ),
        ],
    )
    title = I18nCharField(verbose_name=_('Page title'))
    text = I18nTextField(verbose_name=_('Page content'))
    link_on_frontpage = models.BooleanField(default=False, verbose_name=_('Show link on the event start page'))
    link_in_footer = models.BooleanField(default=False, verbose_name=_('Show link in the event footer'))