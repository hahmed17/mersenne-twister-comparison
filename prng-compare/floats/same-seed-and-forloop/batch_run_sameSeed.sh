mkdir seed_0
cd seed_0
python3 ../../mt-test-forloop.py 0 0
../../mt-test.exe 0 1
../../mt-test.exe 1 1
../../mt-test.exe 2 1
cd ..
sleep 2

mkdir seed_42
cd seed_42
python3 ../../mt-test-forloop.py 42 0
../../mt-test.exe 0 1
../../mt-test.exe 1 1
../../mt-test.exe 2 1
cd ..
sleep 2


for i in {1..3} 
do
    mkdir seed_time$i
    cd seed_time$i
    python3 ../../mt-test-forloop.py null 0
    ../../mt-test.exe 0 0
    ../../mt-test.exe 1 0
    ../../mt-test.exe 2 0
    cd ..
    sleep 2
done