.PHONY: help
help:
	@echo "Available commands:"
	@echo "	 make grafana  -  run grafna in docker"


.PHONY: grafana
grafana:
	docker-compose -f docker-compose-grafana.yml up -d
