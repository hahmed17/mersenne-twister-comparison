cd seed_0
../../mt-test.exe 0
cd ..
sleep 2

cd seed_42
../../mt-test.exe 0
cd ..
sleep 2


for i in {1..3} 
do
	cd seed_time$i
	../../mt-test.exe 0
	cd ..
	sleep 2
done
