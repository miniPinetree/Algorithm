const readline = require('readline');

const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
});
let temp = 0
rl.on('line', function(line){
    for(let i=1;i<Number(line)+1;i++){
        temp+=i;
    }
}).on('close', function(){
    console.log(temp);
process.exit();
});