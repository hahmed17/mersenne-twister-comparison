cd seed_0
..\..\mt-test.exe
cd..
sleep 2

cd seed_42
..\..\mt-test.exe
cd..
sleep 2


for /l %%i in (1, 1, 3) do (
	cd seed_time%%i
	..\..\mt-test.exe
	cd..
	sleep 2
)