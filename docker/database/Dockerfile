FROM postgres:17-alpine

# Copy the dump file to the container's initialization directory
COPY init/monitoring_db_dump.sql /docker-entrypoint-initdb.d/monitoring_db_dump.sql

# Ensure proper permissions for the dump file
RUN chmod 755 /docker-entrypoint-initdb.d/monitoring_db_dump.sql
