#include <iostream>
#include <random>
#include <string>
#include <cmath>
#include <fstream>
#include <numeric>
#include <sstream>
#include <algorithm>
#include <vector>
#include <iterator>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iomanip>

using namespace std;

typedef vector<vector<double>> vvd;

double distEuclid(vector<double> vecA, vector<double> vecB) {
    // Subtract each element of vecB from vecA
    vector<double> vecDiff;
    for (size_t i=0; i < vecA.size(); ++i) {
        vecDiff.push_back(vecA[i] - vecB[i]);
    }
    


    // Square each element of vecDiff and push back to vecDiffSquared
    vector<double> vecDiffSquared(vecDiff.size());
    for (size_t i=0; i < vecDiff.size(); ++i) {
        vecDiffSquared.push_back(pow(vecDiff[i], 2));
    }
    
    // Return square root of the sum of all the elements
    double sumOfDiff = accumulate(vecDiffSquared.begin(), vecDiffSquared.end(), 0.0);  // Get sum of all vector elements
    double sqrtDiff = sqrt(sumOfDiff);
    return sqrtDiff;
}



vvd transpose(const vvd data) {
    int data_rows = data.size();
    int data_cols = data[0].size();

    vvd result(data_cols, vector<double>(data_rows));
    for (vector<double>::size_type i=0; i < data[0].size(); ++i) {
        for (vector<double>::size_type j=0; j < data.size(); ++j) {
            result[i][j] = data[j][i];
        }
    }
    return result;
}




vvd randCent(vvd& dataSet, size_t k, mt19937 gen) {
    // Get num of columns
    int num_col = dataSet[0].size();
    //vvd centroids(k, vector<double>(num_col));
    vvd centroids;
    

    for (size_t j = 0; j < num_col; ++j) {
        // Get values of jth column
        vector<double> colVals(dataSet.size());
        for (size_t i=0; i < dataSet.size(); ++i) {
            colVals[i] = dataSet[i][j];
        }
        

        // Get min and max of column
        auto minimum = min_element(colVals.begin(), colVals.end());
        auto maximum = max_element(colVals.begin(), colVals.end());
        double range = *maximum - *minimum;

        // Create an array of 3 random numbers and push back to centroids
        vector<double> randomFloats;
        randomFloats.reserve(k);

        double rand;
        double randDouble;
        for (size_t i=0; i < k; ++i) {
            rand = gen() / double(gen.max());
            randDouble = *minimum + range*rand;
            randomFloats.push_back(randDouble);
        }
        centroids.push_back(randomFloats);
        randomFloats.clear();
    }

    vvd centroidsTransposed = transpose(centroids);
    return centroidsTransposed;
}






// handles the file input by opening an input filestream to open a string filename
// then puts the values of doubles into a 2 dimensional vector
void handleFile(const string fn, vvd& v)
{
    vector<double> tmp;
    ifstream in;        // input filestream
    in.open(fn);        // open
    string word;
    for (string line; std::getline(in, line); )
    {
        stringstream curs(line);
        while (std::getline(curs, word, ','))
        {
            tmp.push_back(stod(word));
        }
        v.push_back(tmp);
        tmp.clear();
    }

    in.close();              
}





vector<double> KMeans(vvd dataSet, size_t k, mt19937 gen) {
    vector<double> clusterAssignment;

    vvd centroids = randCent(dataSet, k, gen);
    bool clusterChanged = true;

    double minDist;
    int minIndex;
    double dist;
    while (clusterChanged) {
        clusterAssignment.clear();
        clusterChanged = false;
        for (size_t i = 0; i < dataSet.size(); ++i) {
            minDist = numeric_limits<double>::infinity();
            minIndex = -1;
            for (size_t j = 0; j < k; ++j) {
                dist = distEuclid(centroids[j], dataSet[i]);
                if (dist < minDist) {
                    minDist = dist;
                    minIndex = j;
                }
            }
            clusterAssignment.push_back(minIndex);  
            if (clusterAssignment[i] != minIndex) { clusterChanged = true; }
        }


        // Recalculate centroids //

        // Get all points in cluster 
        vvd ptsInClust;
        vector<double> row;
        for (size_t cent = 0; cent < k; ++cent) {
            // Iterate through clusterAssignment and dataSet to get all rows with assignment cent
            for (size_t clust = 0; clust < clusterAssignment.size(); ++clust) {
                if (clusterAssignment[clust] == cent) { // if row is assigned to cluster with cent, add row to ptsInClust
                    row = dataSet[clust];
                    ptsInClust.push_back(row);
                }
            }
            
            // Calculate mean of each data point
            if (ptsInClust.size() != 0) {
                vector<double> ptsInClust_mean;
                vector<double> col;
                double col_mean;
                for (int i = 0; i < ptsInClust[0].size(); ++i) {
                    for (auto& row : ptsInClust) {
                        col.push_back(row[0]);
                    }
                    col_mean = accumulate(col.begin(), col.end(), 0.0) / col.size();
                    ptsInClust_mean.push_back(col_mean);
                    col.clear();
                }
                centroids[cent] = ptsInClust_mean;
            }
            ptsInClust.clear();
        } 
        
    }
    return clusterAssignment;
}




mt19937 mt;

int main(int argc, char *argv[]) {
    unsigned int seed;
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
		seed = stol(seedLine);
	}

	mt.seed(seed); // Set seed


   // Load data sets into vector
    //vvd dataVec;
    vvd X_test;
    //handleFile("datasets/iris.csv", dataVec);
    handleFile("datasets/X_test.csv", X_test);


    // Get true labels from y_test file
    ifstream y_test_file("datasets/y_test.csv");
    istream_iterator<int> start(y_test_file), end;
    vector<double> y_test(start, end);


    // Fit kmeans models
    int k = stoi(argv[1]);
    
    vector<double> labels = KMeans(X_test, k, mt);

    // Get num correct predictions
    size_t num_total = y_test.size();
    size_t num_correct = 0;
    int pred;
    int truth;
    for (size_t i = 0; i < num_total; ++i) {
        pred = labels[i];
        truth = y_test[i];
        if (pred == truth) {
            ++num_correct;
        }
    }


    // Calculate accuracy
    double accuracy = num_correct / double(num_total);
    cout << accuracy << endl;

    ofstream outFile("out-cpp.txt");
    outFile << accuracy << endl;
    outFile.close();

    return 0;
}
