from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...models import Post
from .serializer import PostSerializers
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
# from rest_framework.decorators import action
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .paginations import DefaultPaginations


"""
@api_view(["GET","POST"])
def api_list_view(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        seria = PostSerializers(posts,many=True)
        return Response(seria.data)
    elif request.method == "POST":
        seria = PostSerializers(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data)

"""
# class PostList(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializers
    
#     def get(self,request):
#         posts = Post.objects.filter(status=True)
#         seria = PostSerializers(posts,many=True)
#         return Response(seria.data)
    

#     def post(self,request):
#         seria = PostSerializers(data=request.data)
#         seria.is_valid(raise_exception=True)
#         seria.save()
#         return Response(seria.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=True)
    serializer_class=PostSerializers
    permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['content', 'title']
    pagination_class = DefaultPaginations



    # def list(self,request):
    #     queryset = Post.objects.filter(status=True)
    #     serializer =PostSerializers(queryset,many=True)
    #     return Response(serializer.data)

    # def create(self,request):
    #     seria = PostSerializers(data=request.data)
    #     seria.is_valid(raise_exception=True)
    #     seria.save()
    #     return Response(seria.data)

    # def retrieve(self,request,pk=None):
    #     queryset = Post.objects.filter(status=True)
    #     post = get_object_or_404(queryset, pk=pk)
    #     serializer = PostSerializers(post)
    #     return Response(serializer.data)
    


"""

@api_view(["GET","PUT","DELETE"])
def DetailView(request,id):
    post = Post.objects.get(id=id)
    if request.method == "GET":
        seria = PostSerializers(post)

        return Response(seria.data)
    elif request.method == "PUT":
        seria = PostSerializers(post,data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data)
    elif request.method == "DELETE":
        post.delete()
        return Response("is deleted")

"""
# class PostDetail(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializers
    
#     def get(self,request,id):
#         post = get_object_or_404(Post,pk=id,status=True)
#         seria = self.serializer_class(post)
#         return Response(seria.data)
    
#     def put(self,request,id):
#         post = get_object_or_404(Post,pk=id,status=True)
#         seria = self.serializer_class(post,data=request.data)
#         seria.is_valid(raise_exception=True)
#         seria.save()

#     def delete(self,request,id):
#         post = get_object_or_404(Post,pk=id,status=True)
#         post.delete()
#         return Response("is deleted")
