# grafana-simplejson-dataprovider
This is a Sample implementation for a Data Provider which is using the Grafana Simple Json Data Source


## Development Environment
´´´´bash
docker run \
  -d \
  -p 3000:3000 \
  --name=grafana \
  -e "GF_INSTALL_PLUGINS=grafana-simple-json-datasource" \
  grafana/grafana
´´´´

## Run Sample
````bash
make install
make start
````

docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python your-daemon-or-script.py


## Configure Grafana for Sample Data Source
MAC: http://host.docker.internal:5000
Linux: http://172.17.0.1:5000