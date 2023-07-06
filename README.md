# IoT Sensors Stream Data Visualization

## Project Overview

This project focuses on the visualization of real-time stream data from IoT sensors. By visualizing the data on a dashboard, it provides valuable insights for monitoring and analysis.

The objective is to create a system that simulates stream data from various IoT sensors, stores the data in a database, and visualizes it on a dashboard.

### Purpose and Importance

The purpose of this project is to create a system that simulates stream data from various IoT sensors, stores the data in a database, and visualizes it on a dashboard. This enables real-time monitoring and analysis of IoT sensor data, which can be crucial in applications such as environmental monitoring, industrial automation, and smart city management.

## Project Workflow

The project workflow involves:

1. **Stream Simulation**: the system simulates stream data as IoT sensors by reading the data from a JSON file and publishing it to a Mosquitto topic. This simulates the real-time data generated by IoT sensors.
2. **Stream Storage**: the simulated data is then subscribed and stored in InfluxDB, a time-series database. InfluxDB is ideal for storing and managing time-stamped data efficiently, enabling easy retrieval and analysis.
3. **Stream Visualization**: the stored data is visualized using Grafana, a powerful data visualization tool. Grafana allows for the creation of interactive and customizable dashboards, making it easy to monitor and analyze the real-time data from IoT sensors.

## Technology

- Python
- Eclipse Mosquitto
- InfluxDB
- Grafana
- Docker-compose

## Dataset

 Data from [Hackster.io](https://www.hackster.io/stefanblattmann/real-time-smoke-detection-with-ai-based-sensor-fusion-1086e6#team). It includes the following sensors:

- Air Temperature
- Air Humidity
- TVOC: Total Volatile Organic Compounds; measured in parts per billion (Source)
- eCO2: co2 equivalent concentration; calculated from different values like TVCO
- Raw H2: raw molecular hydrogen; not compensated (Bias, temperature, etc.)
- Raw Ethanol: raw ethanol gas (Source)
- Air Pressure

## Run it

To run this project, follow these steps:

1. Install the required packages

    ```sh
    pip install -r requirements.txt
    ```

2. Prepare the data by converting it from CSV to JSON format

    ```sh
    python csv_to_json_first_100.py
    ```

3. Create the configuration for Mosquitto

    ```sh
    chmod +x create_conf.sh
    ./create_conf.sh
    ```

4. Run the project using Docker-compose

    ```sh
    docker-compose up -d
    ```

5. Run the subscriber script to store the data in InfluxDB

    ```sh
    python influxdb_sub.py
    ```

6. Run the publisher script to simulate the stream data

    ```sh
    python iot_pub.py
    ```

7. Review the data in the InfluxDB bucket by accessing `localhost:8086` in your web browser

8. Create a Grafana dashboard to visualize and customize the data. Access `localhost:3000` in your web browser to get started

## Results and Analysis

After successfully running the project and visualizing the IoT sensor data, several insights can be drawn. For example:

- The real-time monitoring of air temperature and humidity can help identify environmental conditions suitable for various applications.
- The measurement of TVOC and eCO2 levels can aid in detecting air quality issues.
- Raw H2 and ethanol gas measurements can provide valuable information for industrial safety and monitoring.
- The visualization of air pressure can assist in weather forecasting and understanding atmospheric conditions.

These insights demonstrate the value of visualizing IoT sensor data for real-time monitoring and analysis.

## References

- [Dataset Collection from Real Sensors](https://www.hackster.io/stefanblattmann/real-time-smoke-detection-with-ai-based-sensor-fusion-1086e6#team)
- [Eclipse Mosquitto](https://mosquitto.org/)
- [InfluxDB](https://www.influxdata.com/products/influxdb/)
- [Grafana](https://grafana.com/)
- [Docker-compose](https://docs.docker.com/compose/)
