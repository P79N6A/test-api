pid="var/run/test-api.pid)"
if [ -f "$pid" ]; then
    kill $(cat $pid)
fi