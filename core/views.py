from django.shortcuts import get_object_or_404
from .models import Blog
from rest_framework.response import Response

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return Response({'id': blog.id, 'name': blog.name, 'content': blog.content})