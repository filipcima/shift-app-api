if [ -z "$1" ]; then
    echo "mongo ip missing"
    echo "USAGE ./run.sh [mongo-host-ip]"
else
    ip=$1
    docker build -t shift-app-api .
    docker run -i -p 5000:5000 -e MONGODB_URI="mongodb://$IP:27017/shiftapp" shift-app-api
fi



