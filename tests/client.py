from requests.adapters import HTTPAdapter, Retry
from requests import Session


retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])

session = Session()
session.mount('http://', HTTPAdapter(max_retries=retries))
session.mount('https://', HTTPAdapter(max_retries=retries))



def test_one_line():
    url = "http://192.168.3.114:8003/display/text/line"
    data = {"text": "Hello, SSD1306!", "x": 10, "y": 10}
    resp = session.post(url, json=data, timeout=5)
    print(resp.status_code)
    print(resp.json())

def test_chinese_line():
    url = "http://192.168.3.114:8003/display/text/line"
    data = {"text": "你好", "x": 10, "y": 10}
    resp = session.post(url, json=data, timeout=5)
    print(resp.status_code)
    print(resp.json())
    
def test_multi_line():
    url = "http://192.168.3.114:8003/display/text/multiline"
    lines = [
    {"text": "Hello, World!", "x": 0, "y": 0},
    {"text": "192.168.3.123", "x": 0, "y": 18},
    {"text": "255.255.255.255", "x": 0, "y": 36},
    ]
    resp = session.post(url, json=lines, timeout=5)
    print(resp.status_code)
    print(resp.json())

if __name__ == '__main__':
    # test_one_line()
    # test_chinese_line()
    test_multi_line()
        