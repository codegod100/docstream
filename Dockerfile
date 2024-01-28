FROM cgr.dev/chainguard/wolfi-base
WORKDIR /docstream
RUN apk update && apk add pixi bun posix-libc-utils nodejs poetry git
COPY . .

RUN bun install
RUN npm run build
RUN mkdir -p data
RUN poetry install
CMD ./start.sh