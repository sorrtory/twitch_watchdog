FROM python:3.12-slim

WORKDIR /app

RUN mkdir src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./src

CMD ["python", "-m", "src.main"]
