from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from releases.forms import ImportReleaseForm
from releases.excel import save_excel_file


class ImportReleasesView(LoginRequiredMixin, FormView):
    template_name = "release/upload_release.html"
    form_class = ImportReleaseForm
    success_url = reverse_lazy("my_releases")

    def form_valid(self, form):
        file = form.cleaned_data.get("file")
        profile = self.request.user.profile
        import_error = save_excel_file(file, profile)
        # if result contains any error
        if import_error:
            messages.error(self.request, import_error)
            return self.render_to_response(
                self.get_context_data(request=self.request, form=form)
            )
        else:
            return super().form_valid(form)
