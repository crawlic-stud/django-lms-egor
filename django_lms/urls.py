from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from assignments import views
from django_lms import views as project_views
from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView

urlpatterns = [
    url(r'^$', project_views.index, name="home"),
    path('admin/', admin.site.urls),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^assignments/', include('assignments.urls', namespace='assignments')),
    url(r'^resources/', include('resources.urls', namespace="resources")),
    url(r'^user_profile/(?P<pk>[-\w]+)/$',
        project_views.UserProfile.as_view(), name="profile"),
    url('graphql/', FileUploadGraphQLView.as_view(graphiql=True)),
]

# Добавление маршрутов для статических файлов
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
