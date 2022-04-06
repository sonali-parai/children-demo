from django.urls import URLPattern, path
from .views import ChildrenInfoView

from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('CRUD_Test/',ChildrenInfoView.as_view())
]