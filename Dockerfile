FROM python:3.9.13
WORKDIR /api
COPY src ./src
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
CMD ["uvicorn", "src.main.config.app:app", "--reload","--host", "0.0.0.0", "--port", "8000"]