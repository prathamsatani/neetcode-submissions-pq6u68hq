class Solution {
public:

    map<char, int> createHashMap(string& s){
        map<char, int> hashMap;

        for(int i = 0; i < s.length(); i++){
            hashMap[s[i]]++;
        }

        return hashMap;
    }

    bool checkAnagram(map<char, int> hashMap, string& s){

        for(int i = 0; i < s.length(); i++){
            if(hashMap.contains(s[i])){
                hashMap[s[i]]--;
            } else {
                return false;
            }    
        }

        for(auto& pair: hashMap){
            if(pair.second != 0){
                return false;
            }
        }

        return true;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        vector<vector<string>> anagrams;

        vector<bool> used(strs.size(), false);

        for(int i = 0; i < strs.size(); i++){

            if(used[i]) continue;

            vector<string> anagram;
            anagram.push_back(strs[i]);
            used[i] = true;

            map<char, int> hashMap1 = createHashMap(strs[i]);

            for(int j = i + 1; j < strs.size(); j++){

                if(!used[j] && strs[i].length() == strs[j].length()){

                    bool flag = checkAnagram(hashMap1, strs[j]);

                    if(flag){
                        anagram.push_back(strs[j]);
                        used[j] = true;
                    }
                }
            }

            anagrams.push_back(anagram);
        }

        return anagrams;
    }
};