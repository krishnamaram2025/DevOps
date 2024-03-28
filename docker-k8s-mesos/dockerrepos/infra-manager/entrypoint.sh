#!/bin/sh

terraform init .

terraform validate  .

terraform apply  .
