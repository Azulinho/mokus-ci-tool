Download the latest mokus-ci-tool from: https://git.mokus.io/assembly/mokus-ci-tool/pipelines

unzip artifacts.zip and place mokus-ci-tool in the PATH

then


```
mokus-ci-tool new --help
Usage: mokus-ci-tool new [OPTIONS]

Options:
  --template TEXT
  --project-name TEXT
  --git-url TEXT
  --help   

```

executing:

``` 
mokus-ci-tool new --template docker-app --project-name docker-myapp --git-url <gitlab url for my project>
```

will generate a .gitlab-ci.yml, Makefile and a marathon.yaml file locally 

then simply add those to your repo

```
git add .gitlab-ci.yml Makefile marathon.yaml
git commit -m "adding CI build files"
git push
```

and gitlab-ci will automatically build, create a docker image, push to the docker-registry and test-deploy your app on the PaaS as part of the build.
