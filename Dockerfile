FROM python:slim-stretch

WORKDIR /srv

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    make \
    tzdata \
    ca-certificates \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" > /etc/timezone

ADD . .

RUN pip install -U pip && pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["make", "run_all"]