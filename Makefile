PHONY: test
test:
	@echo 'test started...'
	@pytest . -v
PHONY: check
check:
	echo 'code linters started'
	black .
	isort .
	flake8 .
