from django.dispatch import receiver
from django.db.models.signals import post_save

from ..models.post import Post


@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):
    from hashids import Hashids
    import requests
    from bs4 import BeautifulSoup
    if not instance.hash_id:
        hashids = Hashids (salt="djtube", min_length=6)

        instance.hash_id = hashids.encode(instance.id)
        instance.save()

    if created:
        response = requests.get(instance.youtube_original_url)
        soup = BeautifulSoup(response.content, "html.parser")
        title_element = soup.select_one(".watch-title")
        title = title_element.text.strip()

        instance.video_original_title = title
        instance.save()
