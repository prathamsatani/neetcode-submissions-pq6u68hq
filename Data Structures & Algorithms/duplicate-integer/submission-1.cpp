class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::map<int, int> hashMap;
        for(int i = 0; i < nums.size(); i++){
            if(hashMap.contains(nums[i])){
                hashMap[nums[i]]++;
            } else {
                hashMap[nums[i]] = 1;
            }
        }

        for(auto& elem: hashMap){
            if(elem.second > 1){
                return true;
            }
        }

        return false;
    }
};