// 배열(Array)
// Python : 리스트(List)

//index:        0. 1.  2.
let numbers = [10, 20, 30];

console.log(numbers[0]);
console.log(numbers[1]);
console.log(numbers[2]);

//Python: [-1] -> 마지막 요소
// JS : at()
console.log(numbers.at(-1));

// 배열의 원소 개수 - 1 -> 마지막 인덱스(배열의)
console.log(numbers[numbers.length -1]);

//Python: [3] -> IndexError 값이 없기 때문에 
// JS
console.log(numbers[3]);


console.log("===================")
let scores = [82, 95, 77]
for (const [i, score] of scores.entries()) {
    console.log(i + "번째 요소의 값: " + score);
};

// 다양한 데이터 타입을 혼용해서 사용하는 것도 가능
let data = ["hello", 100, true];