package leetcode;

public class No344_Reverse_String {
	 public String reverseString(String s) {
	        int begin=0;
	        int end=s.length()-1;
	        char[] cs = s.toCharArray();
	        char temp;
	        while(begin<=end){
	        	temp=cs[begin];
	        	cs[begin]=cs[end];
	        	cs[end]=temp;
	        	end--;
	        	begin++;
	        }
	 return new String(cs);
	 }
}
