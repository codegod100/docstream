FROM cgr.dev/chainguard/wolfi-base
WORKDIR /app
RUN apk update && apk add pixi bun posix-libc-utils nodejs poetry
COPY package.json .
RUN bun install
COPY . .
RUN npm run build
RUN poetry install
RUN mkdir data
CMD FLASK_DEBUG=1 poetry run flask run --host 0.0.0.0