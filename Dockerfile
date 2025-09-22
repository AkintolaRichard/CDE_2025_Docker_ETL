FROM python:3.10-bookworm

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./utils.py /app/utils.py

COPY ./run_etl_pipeline.py /app/run_etl_pipeline.py

ENTRYPOINT ["python", "run_etl_pipeline.py"]
