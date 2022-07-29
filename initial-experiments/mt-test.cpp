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
#include "srand-rand-function.h"

using namespace std;

static mersenne_twister_engine<uint_fast32_t,
	32, 624, 397, 31, 0x9908b0df, 11, 0xffffffff, 7, 0x9d2c5680, 15, 0xefc60000, 18, 1812433253> generator;


int main() {
	// Seed rand() and mt19937 generator
	ifstream seedFile("seedFile.txt");
	string seedString;
	getline(seedFile, seedString);
	unsigned int seed = stoi(seedString);
	srand(seed);
	generator.seed(seed);

	ofstream randMaxFile("RAND_MAX.txt");
	randMaxFile << RAND_MAX;

	// Generate 10 random numbers from rand()
	ofstream outFile("out-cpp.txt");
	for (size_t i = 1; i <= 10; ++i) {
		outFile << rand() << endl;
	}

	// Generate 10 random numbers from uniform_int_distribution
	ofstream uniformOut("out-cpp-uniform.txt");
	for (size_t i = 1; i <= 10; ++i) {
		uniform_int_distribution<int> dist(0, RAND_MAX);
		int randomNum = dist(generator);
		uniformOut << randomNum << endl;
	}
}

