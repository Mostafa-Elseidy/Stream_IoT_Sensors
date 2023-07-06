mkdir -p mosquitto/config && touch mosquitto/config/mosquitto.conf
mkdir -p mosquitto/data
mkdir -p mosquitto/log

echo "# Basic Mosquitto configuration file

# Set the log destination
log_dest file /var/log/mosquitto/mosquitto.log

# Set the log type
log_type all

# Set the default listener
listener 1883

allow_anonymous true" > mosquitto/config/mosquitto.conf