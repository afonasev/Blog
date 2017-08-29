set -e

pip install -r requirements.txt
isort -c
flake8 backend
pylint backend
py.test --cov=./backend

push="push"

if [ "$TRAVIS_EVENT_TYPE" = "$push" ]; then
    coveralls
    sudo apt-get install sshpass
    sshpass -e ssh root@138.68.65.124 -t supervisorctl restart blog
fi
