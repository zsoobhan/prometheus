from django.views import generic


class BlogView(generic.TemplateView):
    template_name = 'blog/blog.html'
