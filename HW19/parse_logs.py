import apache_log_parser
import argparse
import itertools
import operator
import json

parser = argparse.ArgumentParser(description='Process access.log')
parser.add_argument('-f', dest='file', action='store', help='Path to logfile', default='access.logs')
parser.add_argument('-o', dest='output', action='store', help='output file', default='result.json')
args = parser.parse_args()

requests_by_ip = dict()
requests_by_method = dict()
requests_by_bytes = dict()
requests_by_client_errors = dict()
requests_by_server_errors = dict()

line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")

def collect_requests_by_ip(ip_address):
    if ip_address in requests_by_ip.keys():
        count = requests_by_ip[ip_address] + 1
    else:
        count = 1
    requests_by_ip.update({ip_address: count})


def collect_requests_by_method(http_method):
    if http_method in requests_by_method.keys():
        count = requests_by_method[http_method] + 1
    else:
        count = 1
    requests_by_method.update({http_method: count})


def collect_requests_by_bytes(method, request_url, ip, time, bytes):
    requests_by_bytes.update(
        {
            bytes: {
                'bytes': bytes,
                'method': method,
                'request_url': request_url,
                'ip': ip,
                'time': time}
        }
    )


def collect_client_error_requests(status, method, request_url, ip, time):
    if status.startswith('40'):
        if request_url in requests_by_client_errors.keys():
            count = requests_by_client_errors[request_url]["count"] + 1
        else:
            count = 1
        requests_by_client_errors.update(
            {
                request_url: {
                    'status': status,
                    'count': count,
                    'method': method,
                    'request_url': request_url,
                    'ip': ip,
                    'time': time
                }
            }
        )


def collect_server_error_requests(status, method, request_url, ip, time):
    if status.startswith('50'):
        if request_url in requests_by_server_errors.keys():
            count = requests_by_server_errors[request_url]["count"] + 1
        else:
            count = 1
        requests_by_server_errors.update(
            {
                request_url: {
                    'status': status,
                    'count': count,
                    'method': method,
                    'request_url': request_url,
                    'ip': ip,
                    'time': time
                }
            }
        )


def requests_by_ip_result():
    sorted_d = sorted(requests_by_ip.items(), key=operator.itemgetter(1), reverse=True)
    result = itertools.islice(sorted_d, 10)
    return list(result)


def requests_by_size_result():
    sorted_d = sorted(requests_by_bytes.items(), key=operator.itemgetter(0), reverse=True)
    result = itertools.islice(sorted_d, 10)
    return list(result)


def requests_by_client_error_result():
    sorted_d = sorted(requests_by_client_errors.items(), key=lambda x: x[0][2], reverse=True)
    result = itertools.islice(sorted_d, 10)
    return list(result)


def requests_by_server_error_result():
    sorted_d = sorted(requests_by_server_errors.items(), key=lambda x: x[0][0], reverse=True)
    result = itertools.islice(sorted_d, 10)
    return list(result)


def generate_report(total_requests):
    result = {
        "totalRequests": total_requests,
        "requestsByMethods": requests_by_method,
        'top10requestsByIp': requests_by_ip_result(),
        'top10requestsBySize': requests_by_size_result(),
        'top10ClientErrors': requests_by_client_error_result(),
        'top10ServerErrors': requests_by_server_error_result(),
    }
    return result


def json_to_file(data, file):
    with open(file, 'w') as outfile:
        json.dump(data, outfile)


def proccess_log(file_name, output_file):
    with open(file_name) as file:
        total_requests = 0
        for index, line in enumerate(file.readlines()):
            log_line_data = line_parser(line)
            ip = log_line_data['remote_host']
            method = log_line_data['request_method']
            request_url = log_line_data['request_url']
            status = log_line_data['status']
            response_bytes = log_line_data['response_bytes_clf']
            time = log_line_data['time_received_isoformat']
            collect_requests_by_ip(ip)
            collect_requests_by_method(method)
            collect_requests_by_bytes(method, request_url, ip, time, int(response_bytes))
            collect_client_error_requests(status, method, request_url, ip, time)
            collect_server_error_requests(status, method, request_url, ip, time)
            total_requests = index

        data = generate_report(total_requests)
        json_to_file(data, output_file)


if __name__ == '__main__':
    file = args.file
    output_file = args.output
    proccess_log(file, output_file)
