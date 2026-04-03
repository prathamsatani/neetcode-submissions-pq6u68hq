class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i = 0; i < nums.size() - 1; i++){
            int newTgt = target - nums[i];
            for(int j = i + 1; j < nums.size(); j++){
                if(nums[j] == newTgt){
                    return {i, j};
                }
            }
        }
        return {-1, -1};
    }
};
