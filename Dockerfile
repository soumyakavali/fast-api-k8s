FROM python:3.9
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
COPY ./src /app/src
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]