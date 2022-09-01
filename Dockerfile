FROM ubuntu:20.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        nano \
        python3-dev \
        python3-pip && \
    # Clean image
    apt-get autoremove && \
    apt-get autoclean && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base

COPY /src /app

RUN python3 -m pip --no-cache-dir install --upgrade pip && \
    python3 -m pip config set --global install.trusted-host nexus.olxbr.io && \
    python3 -m pip install -r /app/requirements.txt && \
    # Clean python cache
    find /usr/local/ -name '*.pyc' -print0 | xargs -0 rm -rf || true && \
    find /usr/local/ -type d -name '__pycache__' -print0 | xargs -0 rm -rf || true


WORKDIR /app