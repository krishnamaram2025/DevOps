#!/bin/bash

set +e
cd packer

/usr/bin/packer build builders.json

