# get incomes
curl http://localhost:5000/

# add new income
curl -X POST -H "Content-Type: application/json" -d '{
  "letter": "amoroma"
}' http://localhost:5000/test
