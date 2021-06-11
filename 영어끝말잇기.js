// ## 문제
// https://programmers.co.kr/learn/courses/30/lessons/12981

// ## 접근
// n명의 사람이 순서대로 영어 끝말잇기를 진행한 과정이 words배열에 담겨 전달된다.

// 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는 지를 반환해야 하는 문제

// 끝말잇기 탈락자가 발생하는 경우는 크게 두 가지이다.
// - 이전 단어의 마지막 알파벳으로 시작하는 단어가 아닐 때
// - 이전에 등장한 단어를 말할 때

// ## 코드
// - 코드 가독성과 중복 최소화를 위해** 기능별 함수**를 만들어 풀이하는 것에 재미가 들림 ! 
// 탈락 원인은 두 가지이지만 원인 발생 시 [번호, 차례]를 탐색하는 과정은 공통되기에 이 부분을 함수로 만들어두었다. 
// 중복단어 탐색과정도 함수로 만듦.
// - lastCharOfPrevWord에 직전 단어 마지막 알파벳을 저장한 뒤 탐색하는 단어의 첫 글자와 비교하고 일치하지 않으면 findLoser함수를 실행하여 번호와 차례를 탐색한다.
// - lastCharOfPrevWord 조건에 부합한다면 해당 단어를checkDuplication 함수로 돌려 중복 단어가 존재하는 지 확인한다. 중복 단어를 발견하면 중복 단어 인덱스를 이용하여 findLoser함수를 실행한다.
// - words 요소 반복문이 종료될 때까지 탈락 원인이 발생하지 않았다면 [0,0]을 반환한다!


function solution(n, words) {
    let crrWord = words[0];
    let lastCharOfPrevWord = crrWord[crrWord.length - 1];
    let duplicatedIdx;
    
    function checkDuplication (word) {
        const firstIdx = words.indexOf(word);
        duplicatedIdx = words.indexOf(word, firstIdx + 1);
        
        if (duplicatedIdx === -1) return false;
        
        return duplicatedIdx;
    }
    
    function findLoser (idx) {
        const turn = (idx + 1) % n;
        let iterations = parseInt((idx + 1) / n);
        
        if (turn) iterations += 1;
        
        return [turn? turn:n, iterations];
    }
    
    for (let i = 1; i < words.length; i++) {
        crrWord = words[i];
       
        if (lastCharOfPrevWord !== crrWord[0]) {
            return findLoser(i);
        };
        
        if (checkDuplication(crrWord)) {
            
            return findLoser(duplicatedIdx);
        };
        
        lastCharOfPrevWord = crrWord[crrWord.length - 1];
    };
    
    return [0,0];
}
