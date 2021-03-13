# token PxyJYY8HL1VZK7kWBXQVkHQDiaY2
if [[ -z "$1" ]]; then
    echo "please for testing use create login token"
    exit 0
fi

if [[ $1 == *"create"* ]]; then
    curl -X GET -F 'email=andres@gmail.com' -F 'password=123456' "http://localhost:5000/api/signup"
elif [[ $1 == *"token"* ]]; then
    curl -X GET -F 'email=andres@gmail.com' -F 'password=123456' "http://localhost:5000/api/token"
fi
# add new income

