# Django Celery Beat Status

A library that integrates with django admin and shows in a simple GUI when your periodic are going to run next.

## Instalation

``` bash
pip install django-celerybeat-status
```

## Configuration

1. Add `'celerybeat_status'` to your `INSTALLED_APPS` variable in django settings

``` python
INSTALLED_APPS = [
  ...
  'celerybeat_status',
]
```

2. Create a url for the status check view

```python
from django.conf.urls import url, include

urlpatterns = [
  # other urls...
  url(r'^admin/statuscheck/', include('celerybeat_status.urls', namespace='celerybeat_status')),
]
```

## Usage

Check your tasks under `/admin/statuscheck/periodic-tasks/` (if you configured your urls the way we suggested in this docs).

You can also find a link in `/admin` sidebar.

How you admin page will look like:

![admin-page](https://raw.githubusercontent.com/vintasoftware/django-celerybeat-status/master/README_IMAGES/django-celerybeat-status-admin.png)


How your tasks will be shown:

![tasks-page](https://raw.githubusercontent.com/vintasoftware/django-celerybeat-status/master/README_IMAGES/django-celerybeat-status-tasks.png)


## Commercial Support

This project, as other Vinta open-source projects, is used in products of Vinta clients. We are always looking for exciting work, so if you need any commercial support, feel free to get in touch: contact@vinta.com.br

Copyright (c) 2017 Vinta Serviços e Soluções Tecnológicas Ltda
