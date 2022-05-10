from django.urls       import path
from recordings.views  import CreateView

urlpatterns = [
    path('', CreateView.as_view())
]