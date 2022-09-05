from django.http import JsonResponse


class JsonableResponseMixin:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.accepts('text/html'):
            return response
        return JsonResponse(form.errors.as_json(), status=400)

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.accepts('text/html'):
            return response
        data = {
            'title': self.object.pk,
        }
        return JsonResponse(data)
