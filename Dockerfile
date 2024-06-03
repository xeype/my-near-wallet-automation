FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    wget \
    unzip \
    curl \
    xvfb \
    libxi6 \
    chromium-browser

RUN wget -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/115.0.5790.102/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver_linux64.zip

COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

COPY . /app

WORKDIR /app

ENV PATH /usr/local/bin:$PATH

CMD ["pytest"]
