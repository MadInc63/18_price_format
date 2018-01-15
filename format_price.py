import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Price formatting')
    parser.add_argument(
        'price',
        type=str,
        help='enter price')
    return parser.parse_args()


def format_price(price):
    try:
        if not isinstance(price, (int, float)):
            price = float(price)
        return '{:,.2f}'.format(float(price)).replace(',', ' ').replace(
            '.00',
            ''
        )
    except (ValueError, TypeError):
        return None


if __name__ == '__main__':
    args = parse_args()
    formatted_price = format_price(args.price)
    print(formatted_price)
