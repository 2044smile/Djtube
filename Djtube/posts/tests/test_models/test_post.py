from django.test import TestCase
from django.contrib.auth import get_user_model

from posts.models import Post


class PostModelTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test_password",
        )

        # Create a post
        self.post_video_id = 'djtube'

        self.post = self.user.post_set.create(
            video_id=self.post_video_id,
            title="test_title",
        )

        self.post = self.user.post_set.create(

        )

    def test_post_model_should_have_youtube_original_url(self):
        """
        Post 모델은 가지고 있는 video_id를 이용해서,
        youtube 원본 영상의 링크를 생성할 수 있어야 한다.
        """
        self.assertEqual(
            self.post.get_youtube_original_url(),
            "https://www.youtube.com/watch?v={post_video_id}".format(
                post_video_id=self.post_video_id,
            ),
        )
        pass