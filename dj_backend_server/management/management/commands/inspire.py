# management/commands/inspire.py
from django.core.management.base import BaseCommand
from django.utils.translation import gettext as _
from django.conf import settings
import secrets

class Command(BaseCommand):
    help = _("Displays an inspiring quote")

    def handle(self, *args, **options):
        inspiring_quotes = getattr(settings, 'INSPIRING_QUOTES', [])
        quote = secrets.choice(inspiring_quotes) if inspiring_quotes else _("Don't forget to set INSPIRING_QUOTES in settings.py!")
        self.stdout.write(self.style.SUCCESS(quote))
