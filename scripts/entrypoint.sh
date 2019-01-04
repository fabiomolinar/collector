#!/bin/bash
atd
at now -f ./scripts/deploy.sh
if [ ! -z "$WEBSITE_DJANGO_DEBUG" ] && [ "$WEBSITE_DJANGO_DEBUG" = "True" ]; then
    sed -i "s/debug = off/debug = on/" ./scrapyd/scrapyd.conf
fi
exec "$@"