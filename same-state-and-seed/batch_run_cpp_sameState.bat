cd seed_0
..\..\mt-test.exe 0
..\..\mt-test.exe 1
cd..
timeout 2

cd seed_42
..\..\mt-test.exe 0
..\..\mt-test.exe 1
cd..
timeout 2


for /l %%i in (1, 1, 3) do (
	cd seed_time%%i
	..\..\mt-test.exe 0
	..\..\mt-test.exe 1
	cd..
	timeout 2
)