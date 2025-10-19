from django.core.management.base import BaseCommand
from django.conf import settings
from Hero.models import NPC
import os

class Command(BaseCommand):
    help = 'Удаляет неиспользуемые аватарки'

    def handle(self, *args, **options):
        used_files = set()
        for npc in NPC.objects.exclude(image='').iterator():
            if npc.image:
                used_files.add(npc.image.name)

        avatars_dir = os.path.join(settings.MEDIA_ROOT, 'npc_picks')
        all_files = set()
        for root, dirs, files in os.walk(avatars_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, settings.MEDIA_ROOT)
                all_files.add(rel_path)

        unused = all_files - used_files
        # print(unused)
        for f in unused:
            path = os.path.join(settings.MEDIA_ROOT, f)
            if os.path.exists(path):
                os.remove(path)
                self.stdout.write(f"Удалён: {f}")