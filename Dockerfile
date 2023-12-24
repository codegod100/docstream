FROM debian:bookworm-slim
RUN apt update && apt install -y  curl
ARG PIXI=/root/.pixi/bin/pixi
WORKDIR /workspace/docstream
RUN curl -fsSL https://pixi.sh/install.sh | bash
COPY . .
RUN $PIXI run npx -y bun install
RUN $PIXI run npm run build
CMD $PIXI run server