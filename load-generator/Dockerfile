FROM python:3.11-slim

WORKDIR /app
COPY load_test_dual.py .

RUN pip install requests

CMD ["python", "load_test_dual.py"]