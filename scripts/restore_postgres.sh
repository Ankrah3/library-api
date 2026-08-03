#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: $0 <dump_file_name>"
  exit 1
fi

DUMP_FILE="$1"

if [ ! -f "$DUMP_FILE" ]; then
  echo "Error: Dump file '$DUMP_FILE' not found!"
  exit 1
fi

PGOPTIONS="-c search_path=public" PGPASSWORD='DavidAnkrah123' /usr/lib/postgresql/17/bin/pg_restore \
  -h aws-1-eu-west-2.pooler.supabase.com \
  -p 6543 \
  -U postgres.qvocgbvyjauemxdftdst \
  -d postgres \
  -n public \
  --clean --if-exists \
  --no-owner \
  --no-privileges \
  "$DUMP_FILE"

if [ $? -eq 0 ]; then
  echo "Restore completed successfully from $DUMP_FILE"
else
  echo "Restore FAILED — check the error above"
  exit 1
fi
