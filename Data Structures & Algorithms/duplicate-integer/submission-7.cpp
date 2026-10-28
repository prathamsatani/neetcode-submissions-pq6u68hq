class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> seen;

        for(int num: nums){
            if(seen.find(num) == seen.end()){
                seen[num] = 1;
            } else {
                return true;
            }
        }

        return false;
    }
};