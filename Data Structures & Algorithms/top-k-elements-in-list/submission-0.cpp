class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<pair<int, int>> hashmap;
        map<int, int> hashMap;

        for(int i = 0; i < nums.size(); i++){
            if(hashMap.contains(nums[i])){
                hashMap[nums[i]]++;
            } else {
                hashMap[nums[i]] = 1;
            }
        }

        for(auto pair: hashMap){
            hashmap.push_back(pair);
        }

        std::sort(hashmap.begin(), hashmap.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b){
            return a.second > b.second;
        });

        vector<int> res;
        for(int i = 0; i < k; i++){
            res.push_back(hashmap[i].first);
        }

        return res;
    }
};
