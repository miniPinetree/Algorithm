const readline = require('readline');

const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

rl.on('line', function(line){
    const input = line.split(' ');
    console.log(Number(input[0])+Number(input[1]));
    console.log(Number(input[0])-Number(input[1]));
    console.log(Number(input[0])*Number(input[1]));
    console.log(parseInt(Number(input[0])/Number(input[1])));
    console.log(Number(input[0])%Number(input[1]));

    rl.close();
}).on('close', function(){
    process.exit();
});