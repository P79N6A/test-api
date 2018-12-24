#install virtualenv
pip install virtualenv
#pip install -i http://mirrors.tencentyun.com/pypi/simple --trusted-host mirrors.tencentyun.com virtualenv

if [ ! -d "env" ]; then
    virtualenv env
fi
#export PIP_INDEX_URL=http://mirrors.oa.com/pypi/web/simple
#export PIP_TRUSTED_HOST=mirrors.oa.com

#export PIP_INDEX_URL=http://mirrors.tencentyun.com/pypi/simple
#export PIP_TRUSTED_HOST=mirrors.tencentyun.com

source env/bin/activate && pip install -r requirements.txt
if [ ! -d "var" ]; then
    mkdir var
fi
if [ ! -d "var/log" ]; then
    mkdir var/log
fi
if [ ! -d "var/run" ]; then
    mkdir var/run
fi
if [ ! -d "var/release" ]; then
    mkdir var/release
fi
