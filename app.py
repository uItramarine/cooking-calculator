from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.wsgi import get_wsgi_application

from django.core.management import execute_from_command_line

import sys




settings.configure(
    DEBUG=True,
    SECRET_KEY= '121212',
    ALLOWED_HOSTS=['*'],
    ROOT_URLCONF=__name__,
)


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello world</h1>")

urlpatterns = [
    path("", home_view)
]


application = get_wsgi_application()


if __name__ == "__main__":
    execute_from_command_line(sys.argv)