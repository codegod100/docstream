FROM cgr.dev/chainguard/wolfi-base
RUN apk update && apk add bash curl posix-libc-utils
ENV PIXI=/root/.pixi/bin/pixi
WORKDIR /workspace/docstream
RUN mkdir /workspace/docstream/data
RUN curl -fsSL https://pixi.sh/install.sh | bash
COPY . .
RUN $PIXI run npx -y bun install
RUN $PIXI run npm run build
CMD $PIXI run server