#!/bin/sh

# Replace environment variables in alembic.ini
envsubst < alembic.ini.template > alembic.ini

# Run migrations
exec alembic upgrade head 