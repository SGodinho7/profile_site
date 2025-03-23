FROM python:3.12.8

COPY . /opt/profile_site/
WORKDIR /opt/profile_site

RUN pip install -r requirements.txt
RUN cd profileapp && flask db init && flask db migrate && flask db upgrade

EXPOSE 5000/tcp

ENTRYPOINT ["python", "run.py"]
