# C++ Notes

#### Terminal Commands
```
g++ -std=c++11 -O2 -Wall a.cpp -o a
echo "test" > in
./a < in
cat in
```
`>>` redirects output of command on LHS to the end of the file on the RHS
`>` does the same as `>>`, but replaces RHS instead of appending to it

#### Sublime Layout Formatting
View -> Layout -> 3 Columns
View -> Groups -> Max Columns: 2

#### C++ Starter Template
```C++
#include <bits/stdc++.h>
using namespace std;
int main() {
    // solution comes here
}
```
`#include <bits/stdc++.h>` isn't really best practice, but is convenient for competitive programming

#### Input/Output
```C++
int a, b, x;
cin >> a >> b;
cout << “hi” << "\n" << a;
while (cin >> x) {
    // dynamically sized input
}
```

#### Types
`int` - 32 bit `-2*10^9...2*10^9`
`long long` - 64 bit `-9*10^18...9*10^18` might need LL at the end (not sure)

floats - `double` and `long double`
`printf(“%.9f”, d); // formats to 9 decimal places`
comparing doubles may not be exact use:
`if (abs(a-b) < 1e-9) { // a and b are equal }`

#### Typedefs
```C++
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
```

#### Macros
```C++
#define F first // F = first
#define PB push_back // PB = push_back
#define REP(i,a,b) for (int i = a; i <= b; i++) // macros can have parameters
```

## Data Structures
#### array
```C++
int arr[] = {1,2,3};
int arr[5];
int arr[5] = {1,2,3};
int arr[5] {1};
int arr[3][5]; // multidimensional 3x5 array
```

#### vector
```C++
vector<int> v;
vector<int> v(10, 4); // size 10, default value 4
vector<int> v = {2,3,4};
v[0]; // can index in like a normal array
v.push_back(4);
v.back();
v.pop_back(); // doesn’t return anything?
v.size();
```

#### string
special case of vector, mutable (as opposed to strings in Java, Python, etc)
```C++
string str = "test string";
str.substr(k, x); // [k, k+x)
str1 + str2; // '+' operator
```

#### set
set - balanced binary tree `O(lg n)`, has order
unordered_set - hashset `O(1)`
```C++
set<int> s;
s.insert(5);
s.count(5); // 0 or 1 because of distinct values
s.erase(5);
s.size()
for (auto x : s) {} // works only for set?
s.find(5); // returns iterator pointing to element = 5, iterator will be end if DNE
```
multiset, unordered_multiset also exist

#### map
map - balanced binary tree `O(lg n)`
unordered_map - hash map `O(1)`
```C++
map<string, int> m;
m[“key”] = 5;
m[“dne_key”]; // requesting non existent key adds it with default value
m.count(5);
for (auto x : m) {}
```

#### iterators & ranges
iterator = pointer to an element in a data structure
begin/end = commonly used iterators that point to first element and the position after the last element (half open range)
```C++
// vector ranges
sort(v.begin(), v.end());
reverse(v.begin(), v.end());
random_shuffle(v.begin(), v.end());
// equivalent operations with array
sort(a, a + n);
reverse(a, a + n);
random_shuffle(a, a + n);
```

iterators are often used to access elements of a set
```C++
set<int>::iterator it = s.begin(); // long version
auto it = s.begin(); // short version
cout << *it << "\n"; // dereference pointer
// loop through set using pointer
for (auto it = s.begin(); it != s.end(); it++) {
    cout << *it << "\n";
}
// print largest element in set
auto it = s.end(); it--;
cout << *it << "\n";

s.lower_bound(x); // returns iterator to smallest elt >= than x
s.upper_bound(x); // returns iterator to smallest elt > than x
// both return end if DNE
```

#### lower_bound/upper_bound Functions
```C++
int unsorted[10] = { 3, 3, 2, 1, 5, 5, 4, 3, 7, 8 };
vector<int> v(unsorted, unsorted + 10);
sorted(v.begin(), v.end());
auto k = lower_bound(array,array+n,x)-array;
auto low = lower_bound(v.begin(), v.end(), 3);
auto up = upper_bound(v.begin(), v.end(), 5);
cout << "lower_bound at position " << (low - v.begin()) << '\n'; 
cout << "upper_bound at position " << (up - v.begin()) << '\n';
```

#### Other Data Structures
* Bitset: array of bits `bitset<10> s;`, `s.count();` returns the number of 1's, easy bit operations `a&b|c^d;`
* Deque: dynamic array that is O(1) on ends `deque<int> d;` Has `push_front(x)` and `pop_front()`, which is unavailable with vectors
* Stack: O(1) push/pop; `stack<int> s;`, has `push(x)`, `top()`, and `pop()`
* Queue: O(1) access first/last elt; `queue<int> q;`, `push(x)`, `pop()`, `front()`
* Priority Queue: insertion/retrieval/removal, default max heap; `priority_queue<int> q;`, `push(x)`, `pop()`, `top()`, and `priority_queue<int,vector<int>,greater<int>> q;` for  min heap
* Policy Based Data Structures: data structures not a part of the standard library

#### Codeforces/AtCoder
```
Div 2 > Div 1
Div 1 A = Div 2 C
Div 1 B = Div 2 D
Div 1 C = Div 2 E
AtCoder Beginner Contest (ABC) > 42 has english
R500 - R700 - R900 - R1400
First 15 min - B, 30 min - C
Aim to solve C (ABC) in 10 minutes and D (ABC) in 20 minutes
AtCoder Regular Contect (ARC)
R900 – R1400 – R2100 – R2600
https://kenkoooo.com/atcoder#/table//
https://atcoder.jp/
```

#### Other Notes
assembler - asm -> obj file
compiler - high level prog language -> obj file
`::` is the scope resolution operator
`auto` is a placeholder type

#### Topics Covered
* Sorting
* Binary Search - dictionary method, jumps method