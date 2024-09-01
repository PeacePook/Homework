from src.masks import get_mask_account
from src.masks import get_mask_card_number

if __name__ == '__main__':
    print('Your card number -', get_mask_card_number('7000792289606361'))
    print('Your account number  -', get_mask_account('73654108430135874305'))
