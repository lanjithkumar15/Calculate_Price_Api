from food.models import Pricing

def insert_pricing_data():
    pricing_data = [
        {
            'organization_id': "005",
            'item_id': 1,
            'zone': "north",
            'base_distance_in_km': 6,
            'km_price': 2.0,
            'fix_price': 1200
        },
        {
            'organization_id': "005",
            'item_id': 1,
            'zone': "south",
            'base_distance_in_km': 5,
            'km_price': 1.5,
            'fix_price': 1100
        },
        {
            'organization_id': "005",
            'item_id': 1,
            'zone': "east",
            'base_distance_in_km': 4,
            'km_price': 1.0,
            'fix_price': 1000
        },
        {
            'organization_id': "005",
            'item_id': 1,
            'zone': "west",
            'base_distance_in_km': 3,
            'km_price': 0.8,
            'fix_price': 900
        },
        {
            'organization_id': "005",
            'item_id': 1,
            'zone': "north-east",
            'base_distance_in_km': 7,
            'km_price': 2.2,
            'fix_price': 1300
        },
        {
            'organization_id': "005",
            'item_id': 1,
            'zone': "north-west",
            'base_distance_in_km': 6,
            'km_price': 2.1,
            'fix_price': 1250
        },
        {
            'organization_id': "005",
            'item_id': 1,
            'zone': "south-east",
            'base_distance_in_km': 5,
            'km_price': 1.8,
            'fix_price': 1150
        },
        {
            'organization_id': "005",
            'item_id': 1,
            'zone': "south-west",
            'base_distance_in_km': 4,
            'km_price': 1.3,
            'fix_price': 1050
        },
        {
            'organization_id': "005",
            'item_id': 1,
            'zone': "central-east",
            'base_distance_in_km': 3,
            'km_price': 1.1,
            'fix_price': 950
        },
        {
            'organization_id': "005",
            'item_id': 1,
            'zone': "central-west",
            'base_distance_in_km': 4,
            'km_price': 1.3,
            'fix_price': 1050
        }
    ]

    for data in pricing_data:
        Pricing.objects.create(**data)

if __name__ == "__main__":
    insert_pricing_data()
