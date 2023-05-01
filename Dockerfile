FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt .
COPY example.py .
COPY semantic.py . 
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "semantic.py"]

