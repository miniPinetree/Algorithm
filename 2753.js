const readline = require('readline');

const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

rl.on('line', function(line){
    const year = Number(line);

    if((year%100 !== 0 || year%400 === 0) && year%4 === 0){
        console.log(1);
    }else{
        console.log(0);
    }
    rl.close();
}).on('close', function(){
    process.exit();
});