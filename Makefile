ifeq ($(OS),Windows_NT)
	CC=python
else
	CC=python3
endif

PFLAGS=-3.8-64

TARGET?=src/main
SOURCES:=$(wildcard src/*.py)

.PHONY: all check clean

all:
	$(CC) $(TARGET).py

check:
	python -m py_compile $(SOURCES)

docker:
	docker build -t hue-web-server:latest .
	docker run --network host -ti hue-web-server

dockerclean:
	docker system prune -a

clean:
ifeq ($(OS),Windows_NT)
	@powershell "(Get-ChildItem * -Include *.pyc -Recurse | Remove-Item)"
	@echo Cleaned up .pyc files
else
	@echo "Cleaning up [.pyc] files..."
	@sudo find . -type f -name "*.pyc" -delete
	@echo "Cleaning complete!"
endif
