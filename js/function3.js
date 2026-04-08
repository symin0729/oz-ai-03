// 지금까지 배운 JS문법(조건문, 반복문, 함수 등)을 활용하는 실습

function getAverage(scores) {
    if (scores.lenth === 0) {
        return 0;
    };
    
    let sum = 0;
    for (const score of scores) {
        sum += score
    };
    return sum / scores.lenth;

    // 총합 : ??? (반복문을 돌아서 전부 더하기)
    // 개수 : scores.lenth
    // 평균 = 총합 / 개수
    // return "평균값"
};

const scores = [80, 85, 92, 97]
const average = getAverage(scores)
console.log(average);