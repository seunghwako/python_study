#include <stdio.h>
int main(){
 

    int sum = 0;; // 3의 배수 와 5의 배수를 모두 더한 값

    for(int i=0;i<1000;i++){
       if(i%3==0 || i%5==0){
           sum+=i;
       }
    } 
     printf("%d", sum);
}    