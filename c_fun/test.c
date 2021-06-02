#include <stdio.h>

// #define START 0
// #define LIMIT 300
// #define STEP 20

// int main()
// {
//     float fahr, cels;
//     /*int lower, upper, step;

//     step = 20;
//     upper = 300;
//     lower = 0;

//     fahr = lower;
//     printf("farh   cels\n");
//     while(fahr <= upper){
//         cels = (5.0/9.0) * (fahr-32.0);
//         printf("%3.0f %6.1f\n", fahr, cels);
//         fahr = fahr + step;
//     }

//     cels = lower;
//     printf("cels   farh\n");
//     while(cels <= upper){
//         fahr = ((9.0/5.0) * (cels))+32;
//         printf("%3.0f %6.1f\n", cels, fahr);
//         cels = cels + step;
//     }*/

//     for(fahr = START; fahr <= LIMIT; fahr = fahr + STEP){
//         printf("%3.0f %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
//     }

// }

// int main(){
//     int c;

//     c = getchar();
//     while (c != EOF){
//         putchar(c);
//         c = getchar();
//     }

//     printf("%d", c);
// }

// #define MAX_WORD_SIZE 100
// #define MAX_STACK_SIZE 100

// main(){

//     int i;
//     char c;

//     //Fake entry variable
//     const char word[MAX_WORD_SIZE] = "12-45+*";
   
//     printf();

//     i = 0;
    
//     while((c=gettop()) != 'EOF'){
//         //Do Switch statement for checking what to do  
//         Switch (c){
//             case 0 ... 9:
//                 push(c)
//             case '+':
//                 push(pop() + pop())
//             case '-':
//                 p2 = pop()
//                 push(pop() - p2)
//             case '*':
//                 push(pop() - pop())
//             case '/':
//                 p2 = pop()
//                 if(p2 != 0.0){
//                     push(pop() / p2)
//                 } else{
//                     printf("divid by 0")
//                 }
            
//         }

//     }
// }

// char stack[MAX_STACK_SIZE];

// double pop(){

// }

// void push(){

// }

// char buf[MAX_STACK_SIZE];
// int buffp = 0;

// char getch(){

// }

// char ungetch(){

// }

void main(){
    int x=1, y=2, z[10];
    int *ip;

    ip = &x;
    printf("%p\n", &x);
    printf("%p\n", ip);
    y = *ip;
    printf("%d", y);

}