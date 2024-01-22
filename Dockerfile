FROM cgr.dev/chainguard/wolfi-base
WORKDIR /workspace/docstream
RUN apk update && apk add pixi bun posix-libc-utils nodejs poetry git
COPY package.json .
RUN bun install
COPY . .
RUN npm run build
COPY pyproject.toml .
COPY poetry.lock . 
RUN poetry install
RUN mkdir data
CMD FLASK_DEBUG=1 poetry run flask run --host 0.0.0.0