package leetcode;

public class No476_Number_Complement {
	public int findComplement(int num) {
	        int mask = (Integer.highestOneBit(num) << 1) - 1;
	        num = ~num;
	        return num & mask;
	        }
	}
