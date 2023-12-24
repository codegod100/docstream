FROM debian:stable-slim
RUN apt update && apt install -y curl
ENV PIXI=/root/.pixi/bin/pixi
WORKDIR /workspace/docstream
RUN curl -fsSL https://pixi.sh/install.sh | bash
COPY . .
RUN $PIXI run npm install
CMD $PIXI run start.sh