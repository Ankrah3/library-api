#!/bin/bash
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
FILENAME="backup_mysql_${TIMESTAMP}.sql"

mysqldump \
  -h library-api-mysql-ankrahd75-8ebf.f.aivencloud.com \
  -P 16835 \
  -u avnadmin \
  -p"$MYSQL_PWD"\
  --ssl-mode=REQUIRED \
  --set-gtid-purged=OFF \
  --single-transaction \
  defaultdb > "$FILENAME"

if [ $? -eq 0 ]; then
  echo "Backup saved: $FILENAME"
else
  echo "Backup FAILED — check the error above"
  rm -f "$FILENAME"
  exit 1
fi
