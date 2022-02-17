# Mehrzad Nahavandi
# A01231818


import sys
from reports import device_reporter


def main():
    """ gets user input then returns reports """

    inputs = ['phone', 'tablet', 'laptop']
    reports = ['text', 'json', 'csv']

    if sys.argv[1] not in inputs:
        print('Input type must be either phone, table or laptop.')
    elif sys.argv[2] not in reports:
        print('Report type must be either text, csv or json.')
    else:
        print(device_reporter(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()
