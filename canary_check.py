
import requests, sys

SERVICE_URL = 'http://ai-inference.secure-ai/predict'
TESTS = [{"input": "canary1"}, {"input": "canary2"}]
EXPECTED = 'safe_default'

for t in TESTS:
    r = requests.post(SERVICE_URL, json=t, timeout=2)
    if r.status_code != 200:
        sys.exit(1)
    if r.json().get('prediction') != EXPECTED:
        sys.exit(1)
print('Canary passed')
