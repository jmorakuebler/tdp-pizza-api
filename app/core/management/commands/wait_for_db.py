import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Comando de Django para pausar la ejecución hasta que la base de datos este
    disponible.
    """

    def handle(self, *args, **options):
        self.stdout.write('Esperando base de datos...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write(
                    'Base de datos no disponible, esperando 1 segundo...'
                )
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database disponible!'))
