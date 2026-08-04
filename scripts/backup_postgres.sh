#!/bin/bash
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
FILENAME="backup_postgres_${TIMESTAMP}.dump"

PGPASSWORD="${POSTGRES_PASSWORD}" pg_dump \
  -h "${POSTGRES_HOST}" \
  -p "${POSTGRES_PORT}" \
  -U "${POSTGRES_USER}" \
  -d postgres \
  -n public \
  -F c \
  -f "$FILENAME"

if [ $? -eq 0 ]; then
  echo "Backup saved: $FILENAME"
else
  echo "Backup FAILED — check the error above"
  rm -f "$FILENAME"
  exit 1
fi
