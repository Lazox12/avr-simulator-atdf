
clean:
	rm -rf svd

build:
ifeq ("$(wildcard $(venv))", "")
	python3 -m venv .venv
	./.venv/bin/pip3 install -r requirements.txt
	./.venv/bin/pip3 install -r avr-registers/requirements.txt
endif
	.venv/bin/python avr-registers/gen_registers.py
	.venv/bin/python genSvd.py