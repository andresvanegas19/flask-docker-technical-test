# token PxyJYY8HL1VZK7kWBXQVkHQDiaY2
if [[ -z "$1" ]]; then
    echo "please for testing use create login token"
    exit 0
fi

if [[ $1 == *"create"* ]]; then
    curl -X GET -F 'email=andres@gmail.com' -F 'password=123456' "http://localhost:5000/api/signup"
elif [[ $1 == *"token"* ]]; then
    curl -X GET -F 'email=andres@gmail.com' -F 'password=123456' "http://localhost:5000/api/token"
elif [[ $1 == *"login"* ]]; then
    curl -X GET -H 'authorization: eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ4OTQ5ZDdkNDA3ZmVjOWIyYWM4ZDYzNWVjYmEwYjdhOTE0ZWQ4ZmIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcHl0aG9uLWF1dGgtMTVjMjAiLCJhdWQiOiJweXRob24tYXV0aC0xNWMyMCIsImF1dGhfdGltZSI6MTYxNTU5MDkwMywidXNlcl9pZCI6IjVQbnBKWDYySmFlTWo4dDJ4c2JydkNBZ0xLejIiLCJzdWIiOiI1UG5wSlg2MkphZU1qOHQyeHNicnZDQWdMS3oyIiwiaWF0IjoxNjE1NTkwOTAzLCJleHAiOjE2MTU1OTQ1MDMsImVtYWlsIjoiYW5kcmVzQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhbmRyZXNAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.tlw8rjuYBoUAmd1xeDawdauNgEg-wiAgBVVvSReHprE1KzA_nlBDBMlX4ux8k8FEDlMSmXrPlCwwEPUn0h_W-nizizo8oA4FgQdB4ya4xR42uyQKl3Ff6dYvqNVGQAh2ryJkASOT_Huk0Z51bafXdjPVrdFLUfJUISwM3QJrtnAiTOSKZBXPE-76_5F4DJCBN4IIoLbr-YeG0hZ1jkZkzZOzlJhKx2fSdj9AvMlinGydLw452vEJpldRWtpEU_gx30jutNIPK7vWGuZ2C3XNTPLYWIqwp8c4Z5qWSNyf65LsyBHDNU0204gD_BsiKwzSe1-VKQKA7ZwKnBy0eIbjiQ' "http://localhost:5000/api/userinfo"
fi
