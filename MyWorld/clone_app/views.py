from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.urls import reverse_lazy
from clone_app.models import Post,Comment,Email
from clone_app.forms import PostForm,CommentForm,EmailForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
#### EMAIL ####
from MyWorld.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django import forms

class AboutView(TemplateView):
    template = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'clone_app/post_Detail.html'
    form_class = PostForm

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'clone_app/post_Detail.html'
    form_class = PostForm

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    login_url = '/login/'

class DraftListView(LoginRequiredMixin,ListView):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'clone_app/post_Detail.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')


##################################################################################################
#############################################COMMENTS#############################################


def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
            form = CommentForm()
    return render(request,'clone_app/comment_form.html',{'form':form})


#Send Email
def subscribe(request):
    #sub = EmailForm()
    if request.method == 'POST':
        sub = EmailForm(request.POST)
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['email'].value())
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = True)
        return render(request, 'registration/success.html', {'recepient': recepient})

    else:
        sub = EmailForm()
    return render(request, 'clone_app/about.html', {'form':sub})


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=post.pk)
