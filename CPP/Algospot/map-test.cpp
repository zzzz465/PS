#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(){

	// map
	// <string, int> => <key, value>
	map< int, int > m;


	// insert(key,value)
	m.insert(make_pair(1, 1));
	m.insert(make_pair(2, 2));
	m.insert(make_pair(3, 3));
	m.insert(make_pair(4, 4));
	m.insert(make_pair(5, 5));
	m[6] = 6; // also possible


	// erase(key)
	// m.erase("d");
	// m.erase("e");
	// m.erase(m.find("f")); // also possible


	// empty(), size()
    /*
	if(!m.empty()) cout << "m size: " << m.size() << '\n';


	// find(key)
	cout << "a: " << m.find("a")->second << '\n';
	cout << "b: " << m.find("b")->second << '\n';


	// count(key)
	cout << "a count: " << m.count("a") << '\n';
	cout << "b count: " << m.count("b") << '\n';


	// begin(), end()
	cout << "traverse" << '\n';
    // map< string, int >::iterator it; also possible
	for(auto it = m.begin(); it != m.end(); it++){
		cout << "key: " << it->first << " " << "value: " << it->second << '\n';
	}
    */

	return 0;

}