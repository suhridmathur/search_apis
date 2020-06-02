import requests

from django.conf import settings
from django.core.cache import cache

from rest_framework.response import Response
from rest_framework.views import APIView

from search_apis.mixins import StackOverflowSearchMixin

class SearchAPI(APIView, StackOverflowSearchMixin):
    def get(self, request, *args, **kwargs):
        qs = request._request.META['QUERY_STRING']
        cached_data = self.cache_lookup(qs.lower())
        if cached_data:
            return Response(cached_data)

        response, status_code = self.get_documents(self.SEARCH_API_PATH, qs)
        
        # If success, cache response #
        if status_code == 200:
            self.set_cache(qs.lower(), response)

        return Response(response, status_code)
        

class QuestionDetailAPI(APIView, StackOverflowSearchMixin):
    def get(self, request, *args, **kwargs):
        question_id = kwargs.get('question_id')
        cached_data = self.cache_lookup(question_id)
        if cached_data:
            return Response(cached_data)
        
        response, status_code = self.get_documents_by_id(self.QUESTION_DETAIL_API_PATH, question_id)
        
        # If success, cache response #
        if status_code == 200:
            self.set_cache(question_id, response)
        
        return Response(response, status_code)


class AnswersAPI(APIView, StackOverflowSearchMixin):
    def get(self, request, *args, **kwargs):
        question_id = kwargs.get('question_id')
        cached_data = self.cache_lookup(f'answers_{question_id}')
        if cached_data:
            return Response(cached_data)
        
        response, status_code = self.get_documents_by_id(self.ANSWERS_API_PATH, question_id)
        
        # If success, cache response #
        if status_code == 200:
            self.set_cache(f'answers_{question_id}', response)
        
        return Response(response, status_code)
