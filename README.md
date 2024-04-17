# Grafana + prometheus

## Docker setup

1. Clone repository
2. Run command:
```
sudo docker-compose up -d
```
3. Wait for the project to start
4. Go to the ednpoint `localhost:3000` - `admin:admin`
5. Set data source `prometheus` in data sourceces section - `http://prometheus:9090`
6. Go to the dashboard section and upload `FastAPI_Dashboard.json`
7. Restart charts
8. Use `main.py` in `cd bench` directory
9. You can try use [node-exporter-dashboard](https://grafana.com/grafana/dashboards/1860-node-exporter-full/)
