from django.shortcuts import get_object_or_404
from .models import Blog
from rest_framework.response import Response

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return Response({'id': blog.id, 'name': blog.name, 'content': blog.content})    

def post_blog(request):
    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

def put_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'PUT':
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

def patch_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'PATCH':
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'DELETE':
        blog.delete()
        return Response(status=204)