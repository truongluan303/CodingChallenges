/**
 * @file most_frequent_word.cpp
 *
 * Write a function to find out the most frequent word in a string.
 *
 * The function should receive a sentence (string) and return a word (string)
 * that appears most frequently in the given sentence. If there are more than 1
 * words with the same frequency, return the first one found.
 */

#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;


string most_frequent_word(string sentence)
{
    unordered_map<string, size_t> multiset;
    string curtok = "";

    for (auto ch : sentence)
    {
        if (ch == ' ')
        {
            if (multiset.find(curtok) == multiset.end())
            {
                multiset[curtok] = 0;
            }
            multiset[curtok]++;
            curtok = "";
            continue;
        }
        if (!isalnum(ch))
        {
            continue;
        }
        curtok += tolower(ch);
    }

    string most_freq_word = "";
    size_t most_freq_count = 0;

    for (auto kvp : multiset)
    {
        string word = kvp.first;
        size_t count = kvp.second;

        if (count > most_freq_count)
        {
            most_freq_word = word;
            most_freq_count = count;
        }
    }
    return most_freq_word;
}


int main()
{
    cout << most_frequent_word("Hello, hello again, and again, and again") << endl;
    cout << most_frequent_word("hello there") << endl;
    cout << most_frequent_word("") << endl;

    return 0;
}
