from django.test import RequestFactory

def get_view_context(user, view_class):
    request = RequestFactory().get("/")
    request.user = user
    view = view_class()
    view.setup(request)
    view.object_list = view.get_queryset()

    return view.get_context_data()