import random
import requests
import concurrent.futures


errors = [2,4,5]
endpoint = f'http://localhost:8000/api/v1'

def get_request() -> None:
    response = requests.get(f'{endpoint}/{random.choice(errors)}xx')
    print(response.status_code)


if __name__ == '__main__':
    executor = concurrent.futures.ThreadPoolExecutor()
    try:
        futures = [executor.submit(get_request) for _ in range(100_000)]
        completed, uncompleted = concurrent.futures.wait(futures)
    finally:
        executor.shutdown(wait=False, cancel_futures=True)
