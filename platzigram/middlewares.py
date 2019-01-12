from django.urls import reverse
from django.shortcuts import redirect


class CompletedProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous and not request.user.is_staff:
            profile = request.user.profile

            urls_white_list = [reverse('logout'), reverse('update_profile')]
            if request.path not in urls_white_list:
                if not profile.picture or not profile.biography:
                    return redirect('update_profile')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
