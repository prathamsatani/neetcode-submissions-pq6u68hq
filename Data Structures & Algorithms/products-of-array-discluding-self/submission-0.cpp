class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> sol;
        for(int i = 0; i < nums.size(); i++){
            int currProd = 1;
            for(int j = 0; j < nums.size(); j++){
                if(j != i){
                    currProd *= nums[j];
                }
            }
            sol.push_back(currProd);
        }

        return sol;
    }
};
