FROM python:3.10-alpine
RUN apk add build-base
ENV PYTHONUNBUFFERED=1
ARG BUILD_CONTEXT=backend
COPY ${BUILD_CONTEXT}/requirements.txt requirements.txt
RUN python3 -m ensurepip && \
    python -m pip cache purge && \
    pip install --no-cache-dir -r requirements.txt 
WORKDIR /app
COPY ${BUILD_CONTEXT} backend
ARG PORT
EXPOSE ${PORT}
ENTRYPOINT [ "python3", "backend"]