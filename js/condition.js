// Python: if / elif / else
// If is_student;  //조건식이 와야 함

//JS: if / else if / else -> 결과 : true flase로 boolean 형태로 반환됨
// 첫번째 조건이 실행되면 if문을 탈출하게 됨. 즉 if문이 실행되면 다음 else if문은 실행되지 않음

let age = 20;

if (age >= 19) {

    console.log("성인");  


} else if (age >= 8) {
    console.log("학생");
} else {
    console.log("어린이");
};

// true로 판단되는 값 : 50, 1, -1, "100", "0" => truthy
// flase로 판단되는 값 : 0(num), "", null, undefined(object), NaN => falsy / 타입이 다 다르다
let score = "";
if (score) {
    console.log("점수" + score);
} else {
    console.log("점수 없음");
};

