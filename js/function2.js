// 함수를 값처럼 다루기
// 1) 함수를 변수에 할당할 수 있다

// 함수 정의 -> 설명서/설계도 / 진동벨 설명서
function sayHello() {
    console.log("Hello")
};

// 함수 호출 -> 기능 실제로 사용 / 진동벨 울림 : sayHello(), 매개변수 지정 안함
// sayHello();

// 함수 -> 기능 그 자체 / 진동벨
// sayHello
// console.log(sayHello);

// 함수 자체를 값처럼 변수에 할당할 수 있음
const f = sayHello;
// console.log(f);
// sayHello().    //결과 Hello
//f();              //결과 Hello

// 2) 함수를 다른 함수의 인자로 전달할 수 있음
function run(fn) {
    console.log("start function fun...")
    fn();
    console.log("end function run...")
}

run(sayHello());
// sayHello 함수 자체가 run을 호출하면서 run안의 fn이 sayHello로 들어가서 sayHello호출됨



// (기본) 함수를 선언한 곳에서 직접 호출
// (응용) 함수를 선언하는 곳과 호출하는 곳이 달라짐. 호출은 함수를 누군가한테 준 그 아이들이 알아서 진행함

// numpy 평균 함수
