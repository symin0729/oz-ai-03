const timeInput = document.querySelector("#time-input");
const startBtn = document.querySelector("#start-timer");
const stopBtn = document.querySelector("#stop-timer");
const display = document.querySelector("#timer-display");


// 타이머 아이디

// 초단위로 하는 것을 분단위로 보여주는 것
// 현재 남은 시간(초)를  {분:초} 형태로 출력
let remainingSeconds = 0;


// 599초 -> 9분 59초
function updateDisplay() {
    const min = Math.floor(remainingSeconds / 60);  // 내림 연산
    const sec = remainingSeconds % 60 // 나머지 연산

    // min:1 & sec=9이면  -> 01:09로 변환
    display.textContent =
        String(min).padStart(2, "0")  // 2자릿수를 만들고 없으면 0을 추가하겠다//
    display.className = "fs-3"
}


// Timer 시작
startBtn.addEventListener("click", () => {
    // 이미
    
    
    
    // 유효 : 15
    // 유효하지 않은 값 : 15분, 십오분
    const minuts = Number(timeInput.value);
    if (!minuts || isNaN(minuts) || minuts <= 0) {
        alert("시간을 분 단위(숫자)로 입력하세요.");
        return;
    };

    remainingSeconds = minuts * 60;
    updateDisplay();
    

    // 1초마다 반복적으로 동작하는 함수를 추가
    setInterval(() => {
        remainingSeconds--;
        
        // 남은 시간이 없으면, 타이머 종료
        if (remainingSeconds <= 0){
            resetTimer();
        } else {
            updateDisplay();
        };
        updateDisplay();
    }, 1000);

});

stopBtn.addEventListener("click", resetTimer);

function resetTimer() {
    clearInterval(timeId);
    timerId = null;
};

