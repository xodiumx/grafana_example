# Grafana + prometheus

## Docker setup

- Clone repository

- Run command:

```console
make grafana
```

- Wait for the project to start

- Go to the ednpoint `localhost:3000` - `admin:admin`

- Set data source `prometheus` in data sourceces section - `http://prometheus:9090`

- Go to the dashboard section and upload `fastapi_dashboard_example.json`

- Restart charts

- Use `main.py` in `cd data` directory

- You can try use [node-exporter-dashboard](https://grafana.com/grafana/dashboards/1860-node-exporter-full/)

## Fastapi dashboard

<img width="1500" alt="dash" src="https://github.com/xodiumx/grafana_example/assets/111197771/51831b3d-6080-43bb-8990-8addd8a8d7ae">

## Kafka dashboard

![Kafka](https://github.com/user-attachments/assets/774f17ba-8b46-427a-962b-6254821a1761)
