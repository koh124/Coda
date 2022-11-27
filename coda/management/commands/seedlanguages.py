from django.core.management.base import BaseCommand
from django.conf import settings
from coda.models.models import Language
from coda.models.languages import LANGUAGES_LIST
from datetime import datetime

class Command(BaseCommand):
  def handle(self, *args, **options):
    for i in LANGUAGES_LIST:
      if not Language.objects.filter(name = i).exists():
        Language(
          name = i,
          created_at = datetime.now(),
          updated_at = datetime.now()
        ).save()
        print(f'seeded language name = {i}')
