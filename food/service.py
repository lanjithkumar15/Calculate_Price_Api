from .models import Pricing

class PriceCalculator:
    @staticmethod
    def calculate_total_price(zone, organization_id, total_distance, item_type):
        try:
            pricing = Pricing.objects.get(
                zone=zone,
                organization_id=organization_id,
                item__type=item_type
            )
        except Pricing.DoesNotExist:
            return None
        
        base_distance = pricing.base_distance_in_km
        km_price = pricing.km_price
        fix_price = pricing.fix_price

        total_price = fix_price
        if float(total_distance) > base_distance:
            additional_distance = float(total_distance) - base_distance
            total_price += additional_distance * km_price


        total_price_cents = int(total_price * 100)
        return total_price_cents
