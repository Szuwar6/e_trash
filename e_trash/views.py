from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "homepage.html"


class HomepageClientView(TemplateView):
    template_name = "homepage_client.html"


class HomepageRecyclerView(TemplateView):
    template_name = "homepage_recycler.html"
