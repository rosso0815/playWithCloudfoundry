# Lets test Pivotal Dev

## install a local Pivotal Dev Env

https://github.com/cloudfoundry-incubator/cfdev


```
cf install-plugin -r CF-Community cfdev

cf dev start
# wait 20min

cf login -a https://api.dev.cfdev.sh --skip-ssl-validation



 	    cf login -a https://api.dev.cfdev.sh --skip-ssl-validation
 	
 	Admin user => Email: admin / Password: admin
 	Regular user => Email: user / Password: pass
 	
 	To deploy a particular service, please run:
 	    cf dev deploy-service <service-name> [Available services: mysql]


??? login.local.pcdev.io/login

cf org-users cfdev-org  -a


cf curl "/v2/apps" -X GET -H "Content-Type: application/x-www-form-urlencoded" -d 'q=name:myapp'

cf curl "/v3/apps" -X GET -H "Content-Type: application/x-www-form-urlencoded" 


 python3 -m trace --trace PivotalApi01.py 



## PYTHON

from https://twpower.github.io/214-cf-dev-python-basic-example-en

cf push -m 128M -b python_buildpack python-hello-world

## JAVA

## GO


https://pivotal.io/platform/pcf-tutorials/getting-started-with-pivotal-cloud-foundry-dev/deploy-the-sample-app

```
export JAVA_HOME=/Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home/
export PATH=$JAVA_HOME/bin:$PATH

git clone https://github.com/cloudfoundry-samples/spring-music
cd ./spring-music
cf login -a api.local.pcfdev.io --skip-ssl-validation
user/user
cf logs spring-music --recent
./gradlew assemble
cf push --hostname spring-music
# browse spring-music.dev.cfdev.sh
cf logs spring-music --recent
cf logs spring-music
cf scale spring-music -i 2
cf app spring-music
cf scale spring-music -m 1G
cf scale spring-music -k 512M
```

https://github.com/cloudfoundry-samples/pong_matcher_go

