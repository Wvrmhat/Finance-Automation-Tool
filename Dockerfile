FROM python:3.13-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

# ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit", "run", "main.py"]

