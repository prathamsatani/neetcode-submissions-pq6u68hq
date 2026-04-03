class Solution {
public:
    bool isAnagram(string s, string t) {
        std::map<int, int> hashMap;
        
        for(int i = 0; i < s.size(); i++){
            if(hashMap.contains(s[i])){
                hashMap[s[i]]++;
            } else {
                hashMap[s[i]] = 1;
            }
        }

        for(int i = 0; i < t.size(); i++){
            if(hashMap.contains(t[i])){
                hashMap[t[i]]--;
            } else {
                return false;
            }
        }

        for(auto& p: hashMap){
            std::cout<<p.first<<" "<<p.second<<endl;

            if(p.second != 0){
                return false;
            }
        }

        return true;
    }
};
