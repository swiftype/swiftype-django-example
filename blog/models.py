from django.db import models
from django.db.models import signals
from django.conf import settings
from swiftype import swiftype

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

# Signal handlers

def publish_document(sender, instance, **kwargs):
    client = swiftype.Client(api_key=settings.SWIFTYPE_API_KEY)

    client.create_or_update_document('my-blog', 'posts', {
        'external_id': instance.id,
        'fields': [
            {'name': 'title', 'value': instance.title, 'type': 'string'},
            {'name': 'content', 'value': instance.content, 'type': 'text'},
            {'name': 'url', 'value': "/%s" % instance.slug, 'type': 'enum'},
        ]
    })

def destroy_document(sender, instance, **kwargs):
    client = swiftype.Client(api_key=settings.SWIFTYPE_API_KEY)
    client.destroy_document('my-blog', 'posts', instance.id)

signals.post_save.connect(publish_document, sender=Post)
signals.post_delete.connect(destroy_document, sender=Post)
