from decimal import Decimal
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pricing

class CalculatePriceAPIView(APIView):
    def post(self, request):
        zone = request.data.get('zone')
        organization_id = request.data.get('organization_id')
        total_distance = request.data.get('total_distance')
        item_type = request.data.get('item_type')

        if not total_distance:
            return Response({'error': 'Total distance is missing'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            total_distance = Decimal(total_distance)
        except ValueError:
            return Response({'error': 'Total distance must be a valid number'}, status=status.HTTP_400_BAD_REQUEST)


        pricing = Pricing.objects.filter(zone=zone, organization_id=organization_id).first()
        print()
        
        if not pricing:
            return Response({'error': 'Pricing data not found'}, status=status.HTTP_404_NOT_FOUND)

        base_price = pricing.fix_price
        base_distance = Decimal(pricing.base_distance_in_km)

        if total_distance > base_distance:
            additional_distance = total_distance - base_distance
            total_price = base_price + (additional_distance * pricing.km_price)
        else:
            total_price = base_price

        return Response({'total_price': total_price}, status=status.HTTP_200_OK)
