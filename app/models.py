import base64
import uuid

from django.db import models

HOST_NAME = "http://127.0.0.1:8000/redirect/"


class Url(models.Model):
    url = models.URLField(unique=True)
    url_hash = models.CharField(max_length=256, blank=True)
    short_url = models.URLField(unique=True, blank=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        self.url_hash = self.generate_hash()
        self.short_url = self.create_short_url()
        super(Url, self).save(*args, **kwargs)

    def generate_hash(self):
        hash_ = base64.urlsafe_b64encode(uuid.uuid4().bytes)[:6]
        hash_exist = Url.objects.filter(url_hash=hash_)
        while hash_exist:
            hash_ = base64.urlsafe_b64encode(uuid.uuid4().bytes)[:6]
            hash_exist = Url.objects.filter(url_hash=hash_)
            continue
        hash_ = hash_.decode('utf-8')

        return hash_

    def create_short_url(self):
        return HOST_NAME + self.url_hash
