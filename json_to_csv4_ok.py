from copy import deepcopy
import pandas
import json


def cross_join(left, right):
    new_rows = [] if right else left
    for left_row in left:
        for right_row in right:
            temp_row = deepcopy(left_row)
            for key, value in right_row.items():
                temp_row[key] = value
            new_rows.append(deepcopy(temp_row))
    return new_rows


def flatten_list(data):
    for elem in data:
        if isinstance(elem, list):
            yield from flatten_list(elem)
        else:
            yield elem


def json_to_dataframe(data_in):
    def flatten_json(data, prev_heading=''):
        if isinstance(data, dict):
            rows = [{}]
            for key, value in data.items():
                rows = cross_join(rows, flatten_json(value, prev_heading + '.' + key))
        elif isinstance(data, list):
            rows = []
            for item in data:
                [rows.append(elem) for elem in flatten_list(flatten_json(item, prev_heading))]
        else:
            rows = [{prev_heading[1:]: data}]
        return rows

    return pandas.DataFrame(flatten_json(data_in))


if __name__ == '__main__':
    # with open('response1-3.json') as json_file:
    # with open('response_pse_lokal_dicabut1-2_ok.json') as json_file:
    with open('response_pse_asing_dihentikan_sementara1-2_ok.json') as json_file:
        json_data = json.load(json_file)

    df = json_to_dataframe(json_data)
    # df.to_csv('response1-3b.csv', mode='w')
    # df.to_csv('response1-3c.csv', mode='w')
    # df.to_csv('response_pse_lokal_dicabut1-2_ok.csv', mode='w')
    df.to_csv('response_pse_asing_dihentikan_sementara1-2_ok.csv', mode='w')

    # df = json_to_dataframe(json_data)
    # print(df)
