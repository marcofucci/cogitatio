from django.views.generic import FormView

from braces.views import LoginRequiredMixin

from .forms import AddIdeaForm


class AddIdeaView(LoginRequiredMixin, FormView):
    template_name = 'idea/add.html'
    form_class = AddIdeaForm

    def get_success_url(self):
        return '/'  # TODO change

    def form_valid(self, form):
        form.save(self.request.user)
        return super(AddIdeaView, self).form_valid(form)
