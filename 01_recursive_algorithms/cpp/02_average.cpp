#include <vector>

static int sum(std::vector<int> v, int s) {
    // Check if the vector is empty
    if (v.empty())
        return s; // Return the current sum when the vector is empty

    // Add the last element of the vector to the current sum
    s += v.back();

    // Remove the last element from the vector
    v.pop_back();

    // Recursively call the sum function with the updated vector and sum
    return sum(v, s);
}

double average(const std::vector<int> &v) {
    return sum(v, 0) / (double) v.size();
}