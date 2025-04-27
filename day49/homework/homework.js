//1 სავარჯიშო

let num1 = prompt("Enter Your Number:");
if (num1%2==0) {
    console.log("even")
} else{
    console.log("odd")
}

// სავარჯიშო 2

let num2 = prompt("Enter Your celsius:");
if(num2<=10) {
    console.log("cold")
} else if(num2<=15) {
    console.log("normal")
} else{
    console.log("warm")
}

// სავარჯიშო 3

let num3 = prompt("Enter your grade");
if(num3>=90) {
    console.log("A")
} else if(num3>=80) {
    console.log("B")
} else if(num3>=70) {
    console.log("C")
} else if(num3>=60) {
    console.log("D")
} else {
    console.log("F")
} 

