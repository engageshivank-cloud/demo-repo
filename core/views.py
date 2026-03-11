from django.shortcuts import get_object_or_404
from .models import Blog
from rest_framework.response import Response
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.views import APIView

class BlogDetail(APIView):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return Response(status=204)


class CommentDetail(APIView):

    def post(self, request, blog_pk):
        blog = get_object_or_404(Blog, pk=blog_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(blog=blog)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, blog_pk, pk):
        blog = get_object_or_404(Blog, pk=blog_pk)
        comment = get_object_or_404(blog.comments, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def delete(self, request, blog_pk, pk):
        blog = get_object_or_404(Blog, pk=blog_pk)
        comment = get_object_or_404(blog.comments, pk=pk)
        comment.delete()
        return Response(status=204)
