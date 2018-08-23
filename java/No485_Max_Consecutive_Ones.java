package leetcode;

public class No485_Max_Consecutive_Ones {
    public int findMaxConsecutiveOnes(int[] nums){
    	int count=0,max=0;
    	for (int i=0;i<nums.length;i++){
    		if (nums[i]==1){
    			count++;
    			max=Math.max(count,max);
    		}
    		else count=0;
    	}
    return max;
    }
}
