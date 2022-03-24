FROM kick0131/amazonlinux-iot

WORKDIR /data

COPY .bashrc /root
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

