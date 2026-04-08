// 동등 비교 연산자
// Python : = 할당 / a == b 동일(동등비교)
// JS : a == b
console.log(10 == 10);

let a = 10;
console.log(a == 10);

//Python : false -> type이 달라서 false
// JS : == -> 값만 비교 [내부적으로 타입이 다르면 스스로 만들어 동일하게 만들어냄]
console.log(10 == "10");

// JS : === -> 값 & 타입 비교
console.log(10 === "10");