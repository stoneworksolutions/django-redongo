from django.core.management.base import BaseCommand, CommandError
from redongo import redongo_server
from django.conf import settings
import contextlib
import sys

@contextlib.contextmanager
def redirect_argv(*args):
    sys._argv = sys.argv[:]
    sys.argv = list(args)
    yield
    sys.argv = sys._argv


def get_settings():
    try:
        redongo_settings = {}
        redongo_settings['redis_host'] = settings.REDONGO_REDIS_HOST
        redongo_settings['redis_db'] = settings.REDONGO_REDIS_DB
        redongo_settings['redis_queue'] = settings.REDONGO_REDIS_QUEUE
        return redongo_settings
    except Exception, e:
        raise Exception('Error reading settings: {0}'.format(e))


class Command(BaseCommand):
    help = 'Runs Redongo Server from the info in settings'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.settings = get_settings()

    def handle(self, *args, **options):
        try:
            # Instantiate a server
            with redirect_argv('redongo_server.py', '-r', self.settings['redis_host'], '-d', self.settings['redis_db'], '-q', self.settings['redis_queue'], '-l', '0'):
                redongo_server.main()

        except Exception, e:
            raise CommandError(e)
