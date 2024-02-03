FROM python:alpine
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.7.0 /lambda-adapter /opt/extensions/lambda-adapter

WORKDIR "/var/task"
RUN pip install -r requirements.txt
ADD . /var/task

CMD ["python3", "index.py"]