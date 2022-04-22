FROM python:3.9 as builder

WORKDIR /usr/src/economy

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/economy/wheels -r requirements.txt


FROM python:3.9

# installing netcat (nc) since we are using that to listen to postgres server in entrypoint.bat
RUN apt-get update && apt-get install -y --no-install-recommends netcat && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install dependencies
COPY --from=builder /usr/src/economy/wheels /wheels
COPY --from=builder /usr/src/economy/requirements.txt .
RUN pip install --no-cache /wheels/*

# set work directory
WORKDIR /usr/src/economy/

COPY . .

RUN mkdir  ./logs/
RUN chmod +rwx ./logs/

RUN chmod +x /usr/src/economy/entrypoint.sh
RUN ["chmod", "+x", "/usr/src/economy/entrypoint.sh"]
ENTRYPOINT ["sh", "/usr/src/economy/entrypoint.sh"]