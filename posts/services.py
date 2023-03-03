from typing import List
from datetime import date, timedelta

from django.db.models import Count, F

from .models import Like


class LikesAnalyticService:
    @classmethod
    def get_total_likes_by_day(cls, date_from: str, date_to: str, include_dato_to=True) -> List:
        if include_dato_to:
            date_to = cls._get_included_date(date_to)

        analytics = list(
            Like.objects.filter(date_added__range=(date_from, date_to))
            .annotate(day=F("date_added__date"))
            .values("day")
            .annotate(likes_amount=Count("id"))
            .order_by("day")
        )
        return analytics

    @staticmethod
    def _get_included_date(date_to: str) -> str:
        date_to = (
                date.fromisoformat(date_to) + timedelta(days=1)
        ).strftime("%Y-%m-%d")
        return date_to


