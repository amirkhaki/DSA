//  https://en.wikipedia.org/wiki/Euclidean_algorithm
int gcd(int x, int y) {
    if (y == 0) return x;
    return gcd(y, x % y);
}