FROM sgtwilko/rpi-raspbian-opencv:latest
RUN [ "cross-build-start" ]

RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir flask jsonpickle numpy PiCamera time
COPY server.py .
COPY haarcascade_frontalface_default.xml .
RUN chmod +x server.py
RUN [ "cross-build-end" ]
EXPOSE 5000
CMD ["/usr/bin/python3", "server.py"]
