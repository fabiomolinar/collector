#!/bin/bash
atd
at now -f ./scripts/deploy.sh
exec "$@"