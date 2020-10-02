# covid-guidence
App to track updates on how to make your workplace COVID-secure

## Architecture
Inspired from this [repo](https://github.com/tiangolo/full-stack-fastapi-postgresql):
- fastapi w/ mongodb(?) and celery (rebbitmq)

## Data
Initial data source will be the gov.uk website/content-api on **Working safely during coronavirus**

## Aim
The aim of this project will be to build an application that provides succinct, timely updates on workplace guidance with re. to coronavirus.

## Run app

```

```

## TODO
API:
- [x] setup simple api
- [x] add celery tasks to the api - this [repo](https://github.com/GregaVrbancic/fastapi-celery) may help
- [x] add mongodb(?) connection - this [repo](https://github.com/markqiu/fastapi-mongodb-realworld-example-app) may help

PACKAGING:
- [x] package api, mongodb, celery up using docker

SCRAPING:
- [ ] write scraper interacting with gov.uk content api
