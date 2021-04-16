const readline = require('readline');

const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
});

rl.on('line',function(line){
    const num=Number(line);
    for(let i=1;i<10;i++){
        console.log(num,'*',i,'=',num*i);
    }
    
}).on('close', function(){
    process.exit();
});