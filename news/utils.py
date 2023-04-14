from rest_framework.pagination import CursorPagination
from rest_framework.serializers import Serializer
from rest_framework.response import Response

class CustomPagination(CursorPagination):
    ordering = ['-date']
    page_size = 20 

    def get_paginated_response(self, data):
        # customize the paginate response 
        
        return Response(
            {
                'success':True,
                'links':{
                    'next':self.get_next_link(),
                    'previous':self.get_previous_link()
                },
                'total':len(self.page), 
                'data':data
            }
        )

def create_pagination(queryset, 
                      serializer: Serializer, 
                      request,
                      ):

    assert issubclass(serializer, Serializer)
    paginator = CustomPagination()

    result_page = paginator.paginate_queryset(queryset, request)
    
    result = serializer(result_page, many=True)
    return paginator.get_paginated_response(result.data)
