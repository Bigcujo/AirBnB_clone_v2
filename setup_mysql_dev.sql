#!/bin/bash

# MySQL credentials
MYSQL_ROOT_USER="root"
MYSQL_ROOT_PASSWORD="your_root_password"

# Database and user details
DB_NAME="hbnb_dev_db"
DB_USER="hbnb_dev"
DB_PASSWORD="hbnb_dev_pwd"
PERFORMANCE_SCHEMA_DB="performance_schema"

# Create database if it doesn't exist
mysql -u$MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"

# Create user if it doesn't exist
mysql -u$MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "CREATE USER IF NOT EXISTS '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASSWORD';"

# Grant all privileges on the specified database
mysql -u$MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'localhost';"

# Grant SELECT privilege on the performance_schema database
mysql -u$MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "GRANT SELECT ON $PERFORMANCE_SCHEMA_DB.* TO '$DB_USER'@'localhost';"

# Apply the changes
mysql -u$MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "FLUSH PRIVILEGES;"

echo "MySQL server prepared successfully."

