from django.contrib import admin
from django.urls import path, include
from poll import views as poll_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', poll_views.home, name='home'),
    path('create/', poll_views.create, name='create'),
    path('deleteAll/', poll_views.delete_all, name='deleteAll'),
    path('edit/<poll_id>', poll_views.edit, name='edit'),
    path('delete/<poll_id>', poll_views.delete, name='delete'),
    path('vote/<poll_id>', poll_views.vote, name='vote'),
    path('results/<poll_id>', poll_views.results, name='results'),
]
