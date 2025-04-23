FROM mysql:8.0.42

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=user_db

# Optional: copy init script into the container
COPY init.sql /docker-entrypoint-initdb.d/

# Expose port (optional, for clarity)
EXPOSE 3306