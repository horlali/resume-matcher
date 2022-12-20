FROM python:3.8-slim

EXPOSE 8501

WORKDIR /app

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    build-essential \
    curl \
    git \
    libpq-dev \
    # cache cleaning:
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* 

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN python download_nltk_resource.py
RUN python fileReader.py

CMD [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0" ]
