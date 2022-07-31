#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

unordered_set<string> all_words_collected;

static const unordered_map<unsigned short, vector<char>> kT9Mapping{
  {2, {'a', 'b', 'c'}},
  {3, {'d', 'e', 'f'}},
  {4, {'g', 'h', 'i'}},
  {5, {'j', 'k', 'l'}},
  {6, {'m', 'n', 'o'}},
  {7, {'p', 'q', 'r', 's'}},
  {8, {'t', 'u', 'v'}},
  {9, {'w', 'x', 'y', 'z'}}
};

vector<string> ReadWords() {
  vector<string> valid_words;
  ifstream word_file("/home/coderpad/data/words.txt");
  if (word_file.is_open()) {
    string word;
    while (getline(word_file, word)) {
      valid_words.push_back(word);
    }
    word_file.close();
  }
  return valid_words;
}

/**
 * @brief         A recursive helper function for `GetPossibleWords`
 */
void helper(
  const string&   number_string,    // the string of numbers entered
  const string&   current_str,      // the current string
  unsigned int    depth,            // no. of recursions count
  vector<string>& result            // the result vector
) {
  // If the current depth equals the length of number string,
  // then the word is complete.
  // So add the word to the vector
  // if the word is found in `all_words_collected`
  if (depth == number_string.length()) {
    if (all_words_collected.find(current_str) != all_words_collected.end()) {
      result.push_back(current_str);
    }
    return;
  }
  // Get the digit at the current depth
  // and the letters associated with that digit
  unsigned short  current_digit = number_string[depth] - '0';
  vector<char>    letters       = kT9Mapping.at(current_digit);

  for (char letter : letters) {
    helper(number_string, current_str + letter, depth + 1, result);
  }
}

vector<string> GetPossibleWords(const string& number_string) {
  vector<string> possible_words;
  helper(number_string, "", 0, possible_words);
  return possible_words;
}

int main() {
  string word_list[] = {
      "bat", "ace", "cat", "fact", "hello", "coding", "code",
      "act", "tac", "index", "eat", "world", "programming"
  };
  // initialize the words set
  for (string word : word_list) {
    all_words_collected.insert(word);
  }
  for (string word : GetPossibleWords("46339")) {
    cout << word << " ";
  }
  cout << endl;
  for (string word : GetPossibleWords("228")) {
    cout << word << " ";
  }
  cout << endl;
  return 0;
}

/*
    The solution that I used is to get all possible permutations of the letters and then
  check if that each of them is contained in the words list. Those that are found in the
  word list will then be added to the result vector.

    My solution involved using recursion. And if we look at the base case on line 53, we
  see that it will stop when `depth` is equal to the size of `number_string`. On line
  64, we also see a for loop looping through each letter in the vector of letters
  corresponded to a digit and in that loop we are recursively calling `helper`. But since
  the size of these letters vectors are fixed (we see that they are always either at size
  3 or 4), this loop does not raise the overall time complexity.

    Another thing is that we also do look up in `all_words_collected` on line 54. Since
  `all_words_collected` is an unordered set, the look up time is constant. So this also
  does not raise the time complexity.

    So we conclude that the time complexity for this solution is LINEAR, or O(n) with n
  being the size of `number_string`.
*/
