FROM ubuntu:latest
RUN apt update && apt install -y python3 vim tmux
COPY sender.py /root
COPY receiver.py /root
CMD ["/bin/bash"]
