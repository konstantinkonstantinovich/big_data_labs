run: ## Build and run pandas script in docker container
	docker build -t pandas-bigdata .
	docker run pandas-bigdata

.PHONY: help
help: ## Show list of commands
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'