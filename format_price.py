import argparse
import string


def parse_args():
    parser = argparse.ArgumentParser(description='Price formatting')
    parser.add_argument(
        'price',
        type=str,
        help='enter price')
    return parser.parse_args()


def format_price(price):
    price_characters = set(price)
    letters = set(string.ascii_letters)
    punctuation = set(string.punctuation)
    punctuation.remove('.')
    whitespace = set(string.whitespace)
    for pattern in (letters, punctuation, whitespace):
        if pattern & price_characters or tuple(price).count('.') >= 2:
            return 'Invalid date type. Enter price in float or int.'
    return '{:,.2f}'.format(float(price)).replace(',', ' ').replace('.00', '')


if __name__ == '__main__':
    args = parse_args()
    formatted_price = format_price(args.price)
    print(formatted_price)
