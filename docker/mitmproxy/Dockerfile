FROM mitmproxy/mitmproxy:9.0

RUN pip install protobuf==3.20.3

COPY config/youtube_ad_blocker.py /app/
COPY config/ca/ /root/.mitmproxy/

EXPOSE 8080 443

ENTRYPOINT ["mitmdump", "-s", "/app/youtube_ad_blocker.py", "--listen-port", "8080"]
