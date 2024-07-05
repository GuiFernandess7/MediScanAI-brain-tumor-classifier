FROM ubuntu:20.04

ENV TF_ENABLE_ONEDNN_OPTS=0

LABEL maintainer="guilhermesampaio"

WORKDIR /app

COPY requirements.txt .
COPY . .

#COPY package app/package

EXPOSE 8000

# Instalação de dependências
RUN apt-get update && \
    apt-get install -y \
    libsm6 libxext6 libxrender-dev \
    postgresql-client libpq-dev gcc \
    python3-venv \
    software-properties-common \
    python3.8 \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Instalação de dependências do sistema para psycopg2
RUN apt-get update && \
    apt-get install -y \
    libpq-dev python3-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Criação do ambiente virtual e instalação das dependências do Python
RUN python3.8 -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /app/requirements.txt && \
    /py/bin/pip install ./app/package/tensorflow-2.7.0-cp38-cp38-linux_x86_64.whl

# Configuração de permissões e criação de diretórios
RUN adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static /vol/web/media && \
    chown -R app:app /vol && \
    chown -R app:app /app && \
    chmod -R 755 /vol && \
    chmod -R 755 /app && \
    chmod -R +x ./app/scripts

# Usa o ambiente virtual a cada execução do contêiner
ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD ["/app/app/scripts/run.sh"]