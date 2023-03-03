from datetime import timedelta

from django.test import TestCase
from django.utils.timezone import now

from .factories import LikeFactory
from ..services import LikesAnalyticService


class LikesAnalyticServiceTestCase(TestCase):
    def setUp(self) -> None:
        for day in range(20):
            if day % 2 == 0:  # every even day we have 2 likes
                LikeFactory.create(date_added=(now() + timedelta(days=day)))
            LikeFactory.create(date_added=(now() + timedelta(days=day)))

        self.date_from = now().strftime("%Y-%m-%d")
        self.date_to = (now() + timedelta(days=day)).strftime("%Y-%m-%d")

    def test_get_total_likes_by_day(self):
        analytics = LikesAnalyticService.get_total_likes_by_day(self.date_from, date_to=self.date_to)
        self.assertEqual(len(analytics), 20)
        for i, day in enumerate(analytics):
            if i % 2 == 0:
                self.assertEqual(day.get("likes_amount"), 2)
            else:
                self.assertEqual(day.get("likes_amount"), 1)



