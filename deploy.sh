#! /bin/bash

# XXX: Do this as the ploneconf user so the git keys are all correct!

cd /data/ploneconf/ploneconfbuildout
./bin/buildout -c live.cfg
./bin/client1 restart
./bin/client2 restart
