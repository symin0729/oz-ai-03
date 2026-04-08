// Concat(=Concatenate) -> 문자열을 이어붙이는 연산자

// Python : "hello" + " "  + "world"
// JS :
let firstName = "Alex";
let lastName = "Kim";

console.log(firstName + " " + lastName);

//Python : 10 + "20" => 결과 오류 발생(TypeError) 'int' and 'str' -> 서로 다른 타입을 더하는 것은 어렵다
// JS : 10 + "20" -> "10" + "20" -> "1020" 문자열로 인식해서 + concat 연산 실행
// 타입이 맞지 않으면 형변환이 일어남. 타입 변환이 자동적으로 일어남
console.log(10 + "20");