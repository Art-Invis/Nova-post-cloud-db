import requests
import threading
import time
import sys

# === CONFIG ===
API_URL = "http://nova-post-lb-....eu-west-1.elb.amazonaws.com"     # REST endpoint
WEB_URL = "http://nova-post-lb-....eu-west-1.elb.amazonaws.com/api/health"              # Web UI or landing page
API_THREADS = 40
WEB_THREADS = 20
REPORT_INTERVAL = 5

stop_event = threading.Event()
counter_lock = threading.Lock()
api_requests = 0
web_requests = 0
errors = 0

# === WORKERS ===
def api_worker():
    global api_requests, errors
    s = requests.Session()
    while not stop_event.is_set():
        try:
            r = s.get(API_URL, timeout=5)
            with counter_lock:
                api_requests += 1
            if r.status_code != 200:
                with counter_lock:
                    errors += 1
        except Exception:
            with counter_lock:
                errors += 1

def web_worker():
    global web_requests, errors
    s = requests.Session()
    while not stop_event.is_set():
        try:
            r = s.get(WEB_URL, timeout=5)
            with counter_lock:
                web_requests += 1
            if r.status_code != 200:
                with counter_lock:
                    errors += 1
        except Exception:
            with counter_lock:
                errors += 1

# === REPORTER ===
def reporter():
    last_api = 0
    last_web = 0
    while not stop_event.is_set():
        time.sleep(REPORT_INTERVAL)
        with counter_lock:
            a = api_requests
            w = web_requests
            e = errors
        print(f"[{time.strftime('%H:%M:%S')}] API={a} (+{a-last_api}) | WEB={w} (+{w-last_web}) | ERRORS={e}")
        last_api = a
        last_web = w

# === MAIN ===
if __name__ == "__main__":
    print("Starting dual load test. Ctrl+C to stop.")
    threads = []

    for _ in range(API_THREADS):
        t = threading.Thread(target=api_worker, daemon=True)
        t.start()
        threads.append(t)

    for _ in range(WEB_THREADS):
        t = threading.Thread(target=web_worker, daemon=True)
        t.start()
        threads.append(t)

    rep = threading.Thread(target=reporter, daemon=True)
    rep.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
        stop_event.set()
        time.sleep(1)
        with counter_lock:
            print("Final:", f"API={api_requests}", f"WEB={web_requests}", f"ERRORS={errors}")
        sys.exit(0)