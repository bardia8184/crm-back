from django.db.models import Q
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.core.paginator import Paginator

from .models import Lead
from .serializers import LeadSerializers


@api_view(['POST'])
def new_lead(req):
    data = req.data
    try:
        Lead.objects.create(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            country=data['country'],
            interest=data['interest'],
            remark=data['remark'],
            source=data['source'],
            status=data['status'],
        )
        return JsonResponse({'msg': 'Lead created successfully', 'status': 'success'})
    except Exception as e:
        return JsonResponse({'msg': str(e), 'status': 'error'})


def filter_qs_if_not_None(qs, **kwargs):
    return qs.filter(
        **{key: value for key, value in kwargs.items() if value is not None and value.strip()}
    )


@api_view(['GET'])
def get_all_leads(req):
    query = req.GET['query']
    sort = '-created_at' if req.GET['sort'] == '' or req.GET['sort'] == 'Newest' else 'created_at'

    # data = Lead.objects.all()
    # data = Lead.objects.filter(status=req.GET['status'])
    # data = Lead.objects.filter()
    data = filter_qs_if_not_None(
        Lead.objects.all(),
        status=req.GET['status'],
        source=req.GET['source'],
    ).order_by(sort).filter(Q(name__icontains=query) | Q(email__icontains=query) | Q(phone__icontains=query) |
                            Q(country__icontains=query) | Q(interest__icontains=query) | Q(remark__icontains=query))
    paginator = Paginator(data, 5)  # 5 posts in each page
    current_page = req.GET['current_page']
    items = paginator.page(current_page)
    serializer = LeadSerializers(items, many=True)
    return Response({'data': serializer.data, 'total': paginator.count})
