import java.util.*;
import java.util.regex.*;
import java.text.*;
import java.math.*;
import java.awt.geom.*;

/**
 * This is a Dynamic Programming problem with memoization. The state mark[r][g][b] represents the package needed for packing r red balls, g green balls and b blue balls.
 */

public class PackingBallsDiv2
{
  public static void main(String[] args) {
    System.out.println("Hello World!"); //Display the string.
    PackingBallsDiv2 pb2 = new PackingBallsDiv2();
    System.out.println(pb2.minPacks(78, 53, 64));
  }

 private int[][][] mark;
 public int minPacks(int R, int G, int B)
 {
  mark = new int[R+1][G+1][B+1];
  for(int i=0; i<=R; i++) for(int j=0; j<=G; j++) for(int k=0; k<=B; k++)mark[i][j][k] = -1;
  return solve(R,G,B);
 }
 
 private int solve(int r, int g, int b){
  if(mark[r][g][b] != -1) return mark[r][g][b];
  if(r==0 && g==0 && b==0) return mark[r][g][b] = 0;
  if(r==1 && g==1 && b==1) return mark[r][g][b] = 1;
  mark[r][g][b] = Integer.MAX_VALUE;
  if(r >= 3) mark[r][g][b] = Math.min(mark[r][g][b], 1 + solve(r-3, g, b));
  if(r >= 2) mark[r][g][b] = Math.min(mark[r][g][b], 1 + solve(r-2, g, b));
  if(r >= 1) mark[r][g][b] = Math.min(mark[r][g][b], 1 + solve(r-1, g, b));
  if(g >= 3) mark[r][g][b] = Math.min(mark[r][g][b], 1 + solve(r, g-3, b));
  if(g >= 2) mark[r][g][b] = Math.min(mark[r][g][b], 1 + solve(r, g-2, b));
  if(g >= 1) mark[r][g][b] = Math.min(mark[r][g][b], 1 + solve(r, g-1, b));
  if(b >= 3) mark[r][g][b] = Math.min(mark[r][g][b], 1 + solve(r, g, b-3));
  if(b >= 2) mark[r][g][b] = Math.min(mark[r][g][b], 1 + solve(r, g, b-2));
  if(b >= 1) mark[r][g][b] = Math.min(mark[r][g][b], 1 + solve(r, g, b-1));
  if(r>=1 && g>=1) mark[r][g][b] = Math.min(mark[r][g][b], 1 + solve(r-1, g-1, b));
  if(r>=1 && b>=1) mark[r][g][b] = Math.min(mark[r][g][b], 1 + solve(r-1, g, b-1));
  if(b>=1 && g>=1) mark[r][g][b] = Math.min(mark[r][g][b], 1 + solve(r, g-1, b-1));
  if(r>=1&&g>=1&&b>=1) mark[r][g][b] = Math.min(mark[r][g][b], 1 + solve(r-1, g-1, b-1));
  return mark[r][g][b];
 }
}