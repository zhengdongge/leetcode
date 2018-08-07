package leetcode;

public class No461_Hamming_Distance {
	public static void main(){
	int x=1,y=4;
	System.out.println(hammingDistance(x,y));
	}
public static int hammingDistance(int x, int y) {
    int xor = x ^ y, count = 0;
    for (int i=0;i<32;i++) count += (xor >> i) & 1;
    return count;
}
}

