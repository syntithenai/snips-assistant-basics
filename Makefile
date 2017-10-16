test:
	python setup.py test 
	
installtest:
	snips-install-assistant assistantproj_testsuite.zip
	docker stop snips
	snips&
	sleep 5
	python setup.py test 
	snips-install-assistant assistantproj_GwB7NQG39_basics_suite.zip
	docker stop snips
	snips&
	sleep 5
	
install:
	snips-install-assistant assistantproj_GwB7NQG39_basics_suite.zip
	snips&
	sleep 5
	snipsskills install
	
run:
	snipsskills run
