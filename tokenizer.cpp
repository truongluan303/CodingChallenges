/**
 * Tokenize a string into an array of strings where each string is separated by a given char
 */

#include <iostream>
#include <sstream>
#include <vector>

using namespace std;


vector<string> tokenize(string str, char sep)
{
    size_t start = 0;
    size_t end = str.find(sep);
    vector<string> res;

    while (end != -1)
    {
        res.push_back(str.substr(start, end - start));
        start = end + 1;
        end = str.find(sep, start);
    }
    res.push_back(str.substr(start, end - start));

    return res;
}


int main()
{
    vector<string> tokens = tokenize("This is my string", ' ');
    for (auto word : tokens)
    {
        cout << word << endl;
    }
    return 0;
}
