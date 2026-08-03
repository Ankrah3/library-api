#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: $0 <sql_file_name>"
  exit 1
fi

SQL_FILE="$1"

if [ ! -f "$SQL_FILE" ]; then
  echo "Error: File '$SQL_FILE' not found!"
  exit 1
fi

mysql \
  -h library-api-mysql-ankrahd75-8ebf.f.aivencloud.com \
  -P 16835 \
  -u avnadmin \
  -p"$MYSQL_PWD" \
  --ssl-mode=REQUIRED \
  defaultdb < "$SQL_FILE"

if [ $? -eq 0 ]; then
  echo "Restore completed successfully from $SQL_FILE"
else
  echo "Restore FAILED — check the error above"
  exit 1
fi
