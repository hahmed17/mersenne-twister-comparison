#include <vector>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <fstream>
#include <random>
#include <limits>
#include <sstream>
#include <iterator>
#include <set>

using namespace std;

unsigned int seed;

int main(int argc, char *argv[]) 
{
    // Get PRNG seed
    ifstream seedFile;
    seedFile.open("seedFile.txt");
    if (seedFile.fail()) {  // If no file exists, create one
        // Generate seed from datetime function
        seed = time(NULL);

        // Open a file to store seed
        ofstream seedFile;
        seedFile.open("seedFile.txt");

        // Write seed value to file
        string SeedString = to_string(seed);
        seedFile << SeedString;

        seedFile.close();  // Close seed file
    }
    else {  // If a file exists, set the seed to the stored seed
        string seedLine;
        getline(seedFile, seedLine);
        seed = stoi(seedLine);
    }

    
    // Initialize and seed MT generator
    mt19937 mt(seed);
    //mt.seed(seed);

    // Print state of MT generator
    //cout << mt;

    // Get state from state file
    int sameState = atoi(argv[2]);
    if (sameState == 1) {
        ifstream stateFile("stateFile.txt");
        stateFile >> mt;
    }

    //cout << mt << endl;  // Check state;
    

    // Write generator maximum to file
    ofstream randMaxFile("../../RAND_MAX.txt");
    randMaxFile << mt.max();


    int randGen = atoi(argv[1]);
    // Write 3 random integers and 3 random floats to output files
    if (randGen == 0) {
        ofstream outFile("out-cpp.txt");
        for (size_t i = 1; i <= 5; ++i) {
            outFile << mt() << endl;
        }
    }

    if (randGen == 1) {
        ofstream outFloatFile("out-cpp-float.txt");
        for (size_t i = 1; i <= 5; ++i) {
            uniform_real_distribution<float> float_dist(0, 1);
            outFloatFile << float_dist(mt) << endl;
            double rand2 = float_dist(mt);
        }
    }

    if (randGen == 2) {
        ofstream outUniformFile("out-cpp-uni");
        for (size_t i = 1; i <=5; ++i) {
            uniform_int_distribution<u_int32_t> dist(0, mt.max());
            outUniformFile << dist(mt) << endl;
        }
    }




    // Write 3 random numbers from uniform int distribution to output file
    /*uniform_int_distribution<> uni_dist(0, mt.max());
    ofstream outUni("out-uniform-cpp.txt");
    for (size_t i = 1; i <= 3; ++i) {
        size_t rand_uni = uni_dist(mt);
        outUni << rand_uni << endl;
    }*/
}

