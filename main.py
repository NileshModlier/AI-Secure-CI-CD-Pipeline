
from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest
import time

app = FastAPI(title="Secure AI Inference Service")

REQUEST_COUNT = Counter('ai_requests_total', 'Total AI requests', ['status'])
LATENCY = Histogram('ai_inference_latency_seconds', 'Inference latency')

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/predict')
def predict(payload: dict):
    start = time.time()
    result = {
        'input': payload,
        'prediction': 'safe_default',
        'model_version': 'v1.0'
    }
    LATENCY.observe(time.time() - start)
    REQUEST_COUNT.labels(status='success').inc()
    return result

@app.get('/metrics')
def metrics():
    return Response(generate_latest(), media_type='text/plain')
