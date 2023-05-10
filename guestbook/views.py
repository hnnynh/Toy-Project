from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse 
from django.views.decorators.http import require_http_methods

from .models import Post
import json
# Create your views here.

@require_http_methods(["GET", "POST"])
def post_operation(request):
    if(request.method == "GET"):
        post_json_all = []
        post_list = Post.objects.all()

        for post in post_list:
            post_json_all.append({
                "id" : post.post_id,
                "writer" : post.writer,
                "content" : post.content,
            })

        return JsonResponse({
            'status' : 200,
            'message' : '전체 방명록 조회 성공',
            'data' : post_json_all
        })
    
    if(request.method == "POST"):
        body = json.loads(request.body.decode('utf-8'))

        new_post = Post.objects.create(
            writer = body['writer'],
            content = body['content'],
        )

        new_post_json = {
            "id": new_post.post_id,
            "writer": new_post.writer,
            "content": new_post.content,
        }

        return JsonResponse({
            'status': 200,
            'message': '게시글 생성 성공',
            'data': new_post_json
        })

@require_http_methods(["DELETE"])
def delete_post(request, id):
    delete_post = get_object_or_404(Post, pk = id)
    delete_post.delete()

    return JsonResponse({
        'status': 200,
        'message': '게시글 삭제 성공',
        'data': None
    })