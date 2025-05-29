FROM python:3.12

RUN apt update
RUN apt install -y gettext

COPY ./api/app /
RUN pip3 install -r /requirements.txt

EXPOSE 5001

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app", "--access-logfile", "-", "--error-logfile", "-"]
