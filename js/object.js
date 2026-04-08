// 객체(Object)
// 여러 값에 이름(key)으로 묶어서 관리하는 자료구조
// Python Dictinary와 유사

// key 부분에 "" 안해도 됨
let user = {
    name : "alex",
    age : 40
}

console.log(user.name);
console.log(user["age"]);

// 값 덮어쓰기
user.name = "bob";
console.log(user.name);

console.log("===================")

 for (const key in user) {
    console.log(key, user[key]);
 };
