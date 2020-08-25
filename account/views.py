from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Blog,Talent,Job,Event
# Create your views here.
#blog 
class BlogListView(ListView):
    template_name = "account/blog.html"
    model = Blog
    context_object_name = 'blogs'

    def get_context_data(self, *, object_list=None , **kwargs):
        context = super(BlogListView,self).get_context_data(**kwargs)
        # context["now"] = timezone.now()
        return context

class BlogDetailView(DetailView):
    template_name = "account/blog_detail.html"
    model = Blog
    context_object_name = 'blog'

    def get_context_data(self, *, object_list=None , **kwargs):
        context = super(BlogDetailView,self).get_context_data(**kwargs)
        # context["now"] = timezone.now()
        return context

#talent
class TalentListView(ListView):
    template_name = "account/talent.html"
    model = Talent
    context_object_name = 'talents'

    def get_context_data(self, *, object_list=None , **kwargs):
        context = super(TalentListView,self).get_context_data(**kwargs)
        # context["now"] = timezone.now()
        return context


class TalentDetailView(DetailView):
    template_name = "account/talent_details.html"
    model = Talent
    context_object_name = 'talent'   # better use singular

    def get_context_data(self, *, object_list=None , **kwargs):
        context = super(TalentDetailView,self).get_context_data(**kwargs)
        # context["now"] = timezone.now()
        return context

#job


class JobDetailView(DetailView):
    template_name = "account/job_details.html"
    model = Job
    context_object_name = 'job'

    def get_context_data(self, *, object_list=None , **kwargs):
        context = super(JobDetailView,self).get_context_data(**kwargs)
        # context["now"] = timezone.now()
        return context

class JobListView(ListView):
    template_name = "account/job.html"
    model = Job
    context_object_name = 'jobs'

    def get_context_data(self, *, object_list=None , **kwargs):
        context = super(JobListView,self).get_context_data(**kwargs)
        # context["now"] = timezone.now()
        return context
#event
class EventListView(ListView):
    template_name = "account/event.html"
    model = Event
    context_object_name = 'events'

    def get_context_data(self, *, object_list=None , **kwargs):
        context = super(EventListView,self).get_context_data(**kwargs)
        # context["now"] = timezone.now()
        return context

class EventDetailView(DetailView):
    template_name = "account/event_details.html"
    model = Event
    context_object_name = 'event'

    def get_context_data(self, *, object_list=None , **kwargs):
        context = super(EventDetailView,self).get_context_data(**kwargs)
        # context["now"] = timezone.now()
        return context

# pages
def home(request):

    return render(request,'account/home.html')


def about(request):

    return render(request,'account/about.html')


def talent_details(request):

    return render(request,'account/talent_details.html')


def tc(request):

    return render(request,'account/tc.html')

def pp(request):

    return render(request,'account/pp.html')

def rp(request):

    return render(request,'account/rp.html')


    