FROM ubuntu:latest

ARG TEST_SOURCE
ARG ACCOUNT_ID_1
ARG ACCOUNT_ID_2
ARG ACCOUNT_PASSWORD_1
ARG ACCOUNT_PASSWORD_2
ARG ACCOUNT_PASSPHRASE_1
ARG ACCOUNT_PASSPHRASE_2
ARG ACCOUNT_PK_1
ARG ACCOUNT_PK_2

RUN apt-get update && apt-get install -y software-properties-common \
&& add-apt-repository ppa:deadsnakes/ppa && apt-get install -y python3.10

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    wget \
    unzip \
    curl \
    xvfb \
    libxi6 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-xcb1

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && apt-get install -y google-chrome-stable

RUN wget -O /tmp/chromedriver_linux64.zip https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.141/linux64/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver_linux64.zip

RUN mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/

COPY requirements.txt /tmp/
COPY . /app

WORKDIR /app

RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r /tmp/requirements.txt

ENV PATH /usr/local/bin:$PATH
ENV PATH /app/venv/bin:$PATH
ENV VIRTUAL_ENV="/app/venv"
ENV PYTHONPATH="/app"
ENV TEST_SOURCE=${TEST_SOURCE}
ENV ACCOUNT_ID_1=${ACCOUNT_ID_1}
ENV ACCOUNT_ID_2=${ACCOUNT_ID_2}
ENV ACCOUNT_PASSWORD_1=${ACCOUNT_PASSWORD_1}
ENV ACCOUNT_PASSWORD_2=${ACCOUNT_PASSWORD_2}
ENV ACCOUNT_PASSPHRASE_1=${ACCOUNT_PASSPHRASE_1}
ENV ACCOUNT_PASSPHRASE_2=${ACCOUNT_PASSPHRASE_2}
ENV ACCOUNT_PK_1=${ACCOUNT_PK_1}
ENV ACCOUNT_PK_2=${ACCOUNT_PK_2}

CMD ["bash", "-c", "pytest ${TEST_SOURCE} --alluredir=/app/allure-results"]
