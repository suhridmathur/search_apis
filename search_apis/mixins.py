import requests

from abc import ABCMeta, abstractclassmethod

from django.core.cache import cache

class AbstractSearchMixin(metaclass=ABCMeta):
    """
    Abstract class to be inherited by classes for creating SearchMixins
    for their Web Applications
    Subclasses have to override the `get_documents_by_id` and `get_documents`
    methods.
    """
    @abstractclassmethod
    def get_documents(self, relative_path, query_string=''):
        pass

    @abstractclassmethod
    def get_documents_by_id(self, relative_path, document_id):
        pass

    def get_response_and_status(self, url):
        response = requests.get(url)
        return response.json(), response.status_code
    
    def cache_lookup(self, key):
        return cache.get(key)
    
    def set_cache(self, key, value):
        cache.set(key, value)


class StackOverflowSearchMixin(AbstractSearchMixin):
    """
    To be inherited by StackOverflow class-based Views for utility methods
    """

    BASE_URL='https://api.stackexchange.com/2.2'

    SEARCH_API_PATH='/search/advanced/?site=stackoverflow&'

    QUESTION_DETAIL_API_PATH='/questions/{id}?site=stackoverflow&'

    ANSWERS_API_PATH='/questions/{id}/answers/?site=stackoverflow&'

    def get_documents(self, relative_path, query_string=''):
        url = self.BASE_URL + relative_path + query_string
        return self.get_response_and_status(url) 

    def get_documents_by_id(self, relative_path, id):
        url = self.BASE_URL + relative_path.format(id=id)
        return self.get_response_and_status(url)
