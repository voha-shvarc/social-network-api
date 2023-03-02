from django.utils import timezone

from users.models import User


class TrackLastActiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user = request.user
        if user.is_authenticated:
            self._update_last_active(user)

        return response

    @staticmethod
    def _update_last_active(user: User):
        user.last_active = timezone.now()
        user.save(update_fields=["last_active"])
