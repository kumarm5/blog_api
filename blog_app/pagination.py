from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response


class BlogPagination(pagination.PageNumberPagination):
    page_size = 6

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'page_number': self.page.number,
            'results': data
        })
