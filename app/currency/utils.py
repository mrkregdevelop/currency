from decimal import Decimal


def to_2_places_decimal(value: str) -> Decimal:
    '''
    Convert str value to Decimal with 2 places
        example:
        '123.456' -> Decimal('123.45')
    '''
    return round(Decimal(value), 2)


"""
QA

1.Manual

2.Auto

Dev
3. Unit tests

4. Integration

5. Load

"""
