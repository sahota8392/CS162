#!/bin/sh
echo 'Author check:\n'
head -n5 LemonadeStand.py
echo 'DATE tested:\n'
date
echo '\n'
echo '----------------------------------------------------------\n'
echo 'RUNNING: python3 LemonadeStand.py ----should raise an error-------\n'
python3 LemonadeStand.py

echo '----------------------------------------------------------\n'
echo 'RUNNING: python3 -m unittest LemonadeStandTester.py------------\n'
python3 -m unittest LemonadeStandTester.py

echo '----------------------------------------------------------\n'
echo 'RUNNING: python3 -m unittest tests.py--------------------------\n'
python3 -m unittest tests.py

echo '----------------------------------------------------------\n'
echo 'Finding the if __name__ section of the code...------------------\n'
output=$(grep -n "__name__" "LemonadeStand.py")
line_number=$(echo "$output" | awk -F':' '{print $1}')
echo '\n'
head -n $((line_number + 10)) LemonadeStand.py | tail -n +$((line_number - 9))
echo '\n'

