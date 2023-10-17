install:
	python setup.py install
	make clean

uninstall:
	python setup.py uninstall

reinstall:
	make uninstall
	make install
	make clean

clean:
	rm -Rf build lava_cactus.egg-info dist

test:
	nose2

coverage:
	coverage run --source='.' -m nose2
	coverage html --omit=setup.py
	coverage report --omit=setup.py --fail-under=78

tox-test:
	tox

testw:
	watchmedo shell-command \
		--patterns="*.py;*.txt" \
		--recursive \
		--command='nose2 -x -s --logging-level=CRITICAL --processes=4' \
		.

alltests:
	make clean
	make uninstall
	make install
	make test

.PHONY: test-tox