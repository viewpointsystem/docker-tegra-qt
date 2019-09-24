SHELL := /bin/bash

# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

DBUS_ENV = $(shell dbus-launch)

setup:
	echo "hello"

build: ## Build the container
	docker-compose build qt

shell: 
	export $(DBUS_ENV); docker-compose run qt /bin/bash

run:
	docker-compose run qt
