
// 발견한 규칙
// 가로로 길어질 때는 노란색이 1개당 갈색이 2개씩 증가
// 세로로 길어질 때는 노란색이 2배씩 증가할 때 갈색이 2개씩 증가
// yellow의 가로 길이 * 2 = 모서리를 제외한 상하 brown칸의 개수
// yellow의 세로 길이 * 2 = 모서리를 제외한 좌우 brown칸의 개수
// 마지막에 모서리의 개수 4를 더해준다.

function solution(brown, yellow) {
  let answer;
  let height = Math.floor(Math.sqrt(yellow));
  
  while (true) {
      let cntBrown = (yellow/height+height)*2+4;
      if (cntBrown=== brown) {
          answer = [yellow/height+2, height+2];
          return answer;
      } else if (cntBrown > brown) {
          height++;
      } else {
          height--;
      }
  };

  return answer;
}
