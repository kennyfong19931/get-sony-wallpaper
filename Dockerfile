# Dockerfile
FROM python:alpine

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY get_sony_wallpaper.py .

CMD ["python3","-u","get_sony_wallpaper.py"]