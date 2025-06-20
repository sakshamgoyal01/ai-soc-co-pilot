FROM python:3.10-alpine

# Add troubleshooting tools and a shell
RUN apk update && apk add --no-cache \
    bash \
    iputils \
    busybox-extras \
    gcc \
    libffi-dev \
    python3-dev \
    musl-dev \
    librdkafka-dev

WORKDIR /app

# Copy the script
COPY send_sample_logs.py .

# Install Python dependency
RUN pip install confluent-kafka

# Make logs directory
RUN mkdir -p /logs

# Set default command
CMD ["python", "send_sample_logs.py"]
