#include <stdio.h>
#include <math.h>

long long int reverse(long long int n) {
  long long int result = 0;
  _Bool negative = 0;
  if(n < 0) {
    negative = 1;
    n = -n;
}

  while(n > 0) {
    result *= 10;
    result += n % 10;
    n /= 10;
  }
  if(negative)
    return -result;
  return result;
}

int main(void) {
  long long int n;
  long long int result;

  printf("Enter an integer\n");
  scanf("%lli", &n);
  printf("The reverse of %lli is %lli\n", n, reverse(n));

  return 0;
}
