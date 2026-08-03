#!/bin/bash
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
FILENAME="backup_postgres_${TIMESTAMP}.dump"

PGPASSWORD='DavidAnkrah123' pg_dump \
  -h aws-1-eu-west-2.pooler.supabase.com \
  -p 6543 \
  -U postgres.qvocgbvyjauemxdftdst \
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
