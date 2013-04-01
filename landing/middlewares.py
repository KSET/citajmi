from django.shortcuts import redirect
from landing.views import landing_page

class LandingPageMiddleware:

    def process_request(self, request):
        if request.path != '/':
            return None
        skip = request.session.get('skip', False)
        if skip:
            return redirect('myflatpages:home')
        return redirect(landing_page)
