FROM cgr.dev/chainguard/wolfi-base
WORKDIR /docstream
RUN apk update && apk add pixi bun posix-libc-utils nodejs poetry git
COPY . .

RUN bun install
RUN npm run build

RUN poetry install

RUN mkdir data
CMD FLASK_DEBUG=1 poetry run flask run --host 0.0.0.0