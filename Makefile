# vim:filetype=make shiftwidth=4 tabstop=4 noexpandtab

# if CI_BUILD_REF is not set, as not running in CI
# then set it to 'local'
CI_BUILD_REF ?= local

clean:
	docker rmi test123:$(CI_BUILD_REF) || echo

build:
	echo "building docker image: test123:$(CI_BUILD_REF)"
	docker build -t $$DOCKER_REGISTRY_ENDPOINT/test123:$(CI_BUILD_REF) .

publish:
	echo "pushing docker image: test123:$(CI_BUILD_REF) to registry $(DOCKER_REGISTRY_ENDPOINT)"
	docker login --username=$(DOCKER_REGISTRY_USERNAME) --password=$(DOCKER_REGISTRY_PASSWORD)  $(DOCKER_REGISTRY_ENDPOINT)
	docker push $(DOCKER_REGISTRY_ENDPOINT)/test123:$(CI_BUILD_REF)

deploy: yaml2json marathonctl
	echo "deploying marathon service: ci-builds/test123/$(CI_BUILD_REF)/docker-app"
	# update marathon.json file with correct CI_BUILD_REF
	sed -i s/local/$(CI_BUILD_REF)/g marathon.yaml
	mkdir -p output
	cat marathon.yaml | ./yaml2json | jq '.apps.app' > output/app.json
	./marathonctl --host http://marathon.mesos:8080 deploy output/app.json

	
yaml2json:
	@wget -O yaml2json -c https://github.com/bronze1man/yaml2json/blob/master/builds/linux_amd64/yaml2json?raw=true
	@chmod 755 yaml2json


marathonctl:
	@wget -O marathonctl -c https://github.com/ashwanthkumar/marathonctl/releases/download/v0.0.3-fix/marathonctl-linux-amd64	
	@chmod 755 marathonctl