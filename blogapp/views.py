from django.shortcuts import render_to_response
from django.template import RequestContext
from blogapp.models import Post
import datetime

def index(request):
    if request.method == 'POST':
        # save new post
        title = request.POST['title']
        content = request.POST['content']

        post = Post(title=title)
        post.last_update = datetime.datetime.now() 
        post.content = content
        post.save()

    # Get all posts from DB
    posts = Post.objects
    return render_to_response('blogapp/index.html', {'Posts': posts},
                              context_instance=RequestContext(request))


def update(request):
    id = eval("request." + request.method + "['id']")
    post = Post.objects(id=id)[0]
    
    if request.method == 'POST':
        # update field values and save to mongo
        post.title = request.POST['title']
        post.last_update = datetime.datetime.now() 
        post.content = request.POST['content']
        post.save()
        template = 'blogapp/index.html'
        params = {'Posts': Post.objects} 

    elif request.method == 'GET':
        template = 'blogapp/update.html'
        params = {'post':post}
   
    return render_to_response(template, params, context_instance=RequestContext(request))
                              

def delete(request):
    id = eval("request." + request.method + "['id']")

    if request.method == 'POST':
        post = Post.objects(id=id)[0]
        post.delete() 
        template = 'blogapp/index.html'
        params = {'Posts': Post.objects} 
    elif request.method == 'GET':
        template = 'blogapp/delete.html'
        params = { 'id': id } 

    return render_to_response(template, params, context_instance=RequestContext(request))
                              
    
