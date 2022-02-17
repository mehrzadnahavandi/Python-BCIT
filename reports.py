# Mehrzad Nahavandi
# A01231818

import time
import statistics
import data

def device_reporter(device_name, report_type):
    """ gets info from data then changes the format then returns them """

    now = time.strftime("%Y-%m-%d %H:%M", time.gmtime())

    if device_name == 'phone':
        raw_data = data.get_phone_info_list()
    elif device_name == 'tablet':
        raw_data = data.get_tablet_info_list()
    elif device_name == 'laptop':
        raw_data = data.get_laptop_info_list()


    if report_type == 'text':
        prices_list_text = []
        ram_list_text = []
        os_names_text = []
        total = len(raw_data)
        for i in raw_data:

            entry = i.split(',')
            prices_list_text.append(float(entry[6]))
            ram_list_text.append(float(entry[3]))
            os_names_text.append(str(entry[4] + ' ' + entry[5]))

        text = 'Timestamp: ' + now + "\n"\
                + 'Device: ' + device_name + "\n"\
                + 'Number: ' + str(total) + "\n"\
                + 'Avarage Price: ' + str(sum(prices_list_text)/len(prices_list_text)) + "\n"\
                + 'Minimum Price: ' + str(min(prices_list_text)) + "\n"\
                + 'Maximum Price: ' + str(max(prices_list_text)) + "\n"\
                + 'Median RAM: ' + str(statistics.median(ram_list_text)) + "\n"\
                + 'Operating Systems: ' + ', '.join(os_names_text)



    if report_type == 'csv':
        prices_list_csv = []
        ram_list_csv = []
        os_names_csv = []
        total = len(raw_data)
        for i in raw_data:

            entry = i.split(',')
            prices_list_csv.append(float(entry[6]))
            ram_list_csv.append(float(entry[3]))
            os_names_csv.append(str(entry[4] + ' ' + entry[5]))

        text = now + ',' \
                + device_name + ',' \
                + str(total) + ',' \
                + str(sum(prices_list_csv)/len(prices_list_csv)) + ',' \
                + str(min(prices_list_csv)) + ',' \
                + str(max(prices_list_csv)) + ',' \
                + str(statistics.median(ram_list_csv))+ ',' \
                + '"' + ', '.join(os_names_csv) + '"'

    if report_type == 'json':
        prices_list_json = []
        ram_list_json = []
        os_names_json = []
        total = len(raw_data)
        for i in raw_data:

            entry = i.split(',')
            prices_list_json.append(float(entry[6]))
            ram_list_json.append(float(entry[3]))
            os_names_json.append(str(entry[4] + ' ' + entry[5]))

        text = '{'\
            + '"date_time": "' + now + '",'\
            + '"device_type": "' + device_name + '",'\
            + '"number": ' + str(total) + ','\
            + '"avarage_price": ' + str(sum(prices_list_json)/len(prices_list_json)) + ','\
            + '"min_price": ' + str(min(prices_list_json)) + ','\
            + '"max_price": ' + str(max(prices_list_json)) + ','\
            + '"median_ram": ' + str(statistics.median(ram_list_json)) + ','\
            + '"operating_systems": [' + ', '.join(f'"{o}"' for o in os_names_json) + ']}'

    return(text)
