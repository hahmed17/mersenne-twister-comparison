for /l %%i in (1, 1, 100) do (
    mkdir sample%%i
    cd sample%%i
    cat ..\..\seeds.txt | head -%%i | tail -1 > seedFile.txt
    ..\..\kmeans.exe 3 ..\..\datasets\iris.txt 
    cd ..
    timeout 5
)