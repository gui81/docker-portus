FROM library/rails:4.2
MAINTAINER Lucas Johnson <lucasejohnson@netscape.net>

EXPOSE 3000

RUN apt-get update && \
    apt-get install -y python-yaml && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/SUSE/Portus.git /portus

WORKDIR /portus
RUN bundle install --retry=3

COPY init.py /portus/init.py
ENTRYPOINT ["python", "/portus/init.py"]
CMD ["puma", "-b", "tcp://0.0.0.0:3000", "-w", "3"]
