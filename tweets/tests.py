from django.contrib.auth.models import User
from django.test import TestCase
from tweets.models import Tweet
from datetime import timedelta
from utils.time_helpers import utc_now


class TweetTests(TestCase):

    def test_hours_to_now(self):
        nanzhou = User.objects.create_user(username='nanzhou')
        tweet = Tweet.objects.create(user=nanzhou, content='nanzhou Data Good!')
        tweet.created_at = utc_now() - timedelta(hours=10)
        tweet.save()
        self.assertEqual(tweet.hours_to_now, 10)
