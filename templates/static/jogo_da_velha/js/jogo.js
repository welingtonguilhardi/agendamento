let boxOne = document.getElementById('boxOne');
let boxTwo = document.getElementById('boxTwo')
let boxThree = document.getElementById('boxThree')
let boxFour = document.getElementById('boxFour')
let boxFive = document.getElementById('boxFive')
let boxSix = document.getElementById('boxSix')
let boxSeven = document.getElementById('boxSeven')
let boxEight = document.getElementById('boxEight')
let boxNine = document.getElementById('boxNine')
let TimeUser = document.getElementById('user')

let checkBoxUserOne = []; // array respondavel por verificar quais divs foram apertadas pelo usuario um
let checkBoxUserTwo = []; // array respondavel por verificar quais divs foram apertadas pelo usuario dois
let user = 0 // variavel responsavel por determinar de quem é a vez 
let win = false // variavel responsavel por determinar se houve um vencendor 

let boxOneClick = false // variavel responsavel por verificar se o campo já foi acionado
let boxTwoClick = false // variavel responsavel por verificar se o campo já foi acionado
let boxThreeClick = false // variavel responsavel por verificar se o campo já foi acionado
let boxFourClick = false // variavel responsavel por verificar se o campo já foi acionado
let boxFiveClick = false // variavel responsavel por verificar se o campo já foi acionado
let boxSixClick = false // variavel responsavel por verificar se o campo já foi acionado
let boxSevenClick = false // variavel responsavel por verificar se o campo já foi acionado
let boxEightClick = false // variavel responsavel por verificar se o campo já foi acionado
let boxNineClick = false // variavel responsavel por verificar se o campo já foi acionado




function CheckTied() {

    if (boxOneClick && boxTwoClick && boxThreeClick && boxFourClick && boxFiveClick && boxSixClick && boxSevenClick && boxEightClick && boxNineClick && !win){
        alert("Empate")
        window.location.reload(true); //recarrega a pagina
    }

}


function userClick (box,btn){
    if ( user === 0 || user ===2 || user === 4 || user === 6 || user === 8){
        getBox(1,box,btn)
        TimeUser.innerHTML = "Usuario 2"
    }else{
        getBox(2,box,btn)
        TimeUser.innerHTML = "Usuario 1"
    }
    user = user + 1
}

function getBox(user,box,btn) {
    if (user === 1){
        box.innerHTML = "x"
    }else{
        box.innerHTML = "o"
    }
    checkWin(user,btn)
}

function checkWin(user,btn){
    if (user === 1){
        checkBoxUserOne.push(btn) //adiciona o metodo do botão para minha array

        resOne = checkBoxUserOne.indexOf("btnOne") // variavel responsavel por verificar se o usuario 1 já apertou na minha 01
        resTwo = checkBoxUserOne.indexOf("btnTwo") // variavel responsavel por verificar se o usuario 1 já apertou na minha 02
        resThree = checkBoxUserOne.indexOf("btnThree") // variavel responsavel por verificar se o usuario 1 já apertou na minha 03
        resFour = checkBoxUserOne.indexOf("btnFour") // variavel responsavel por verificar se o usuario 1 já apertou na minha 04
        resFive = checkBoxUserOne.indexOf("btnFive") // variavel responsavel por verificar se o usuario 1 já apertou na minha 05
        resSix = checkBoxUserOne.indexOf("btnSix") // variavel responsavel por verificar se o usuario 1 já apertou na minha 06
        resSeven = checkBoxUserOne.indexOf("btnSeven") // variavel responsavel por verificar se o usuario 1 já apertou na minha 07
        resEight = checkBoxUserOne.indexOf("btnEight") // variavel responsavel por verificar se o usuario 1 já apertou na minha 08
        resNine = checkBoxUserOne.indexOf("btnNine") // variavel responsavel por verificar se o usuario 1 já apertou na minha 09
        if (
            resOne != -1 && resFive != -1 && resNine != -1
            || resThree != -1 && resFive!= -1 && resSeven != -1

             || resOne != -1 && resFour != -1 && resSeven != -1 
             || resTwo != -1 && resFive != -1 && resEight != -1
             || resThree != -1 && resSix != -1 && resNine != -1 

             || resOne != -1 && resTwo != -1 && resThree != -1 
             || resFour!= -1 && resFive != -1 && resSix!= -1 
             || resSeven!= -1 && resEight!= -1 && resNine != -1 
            ) {
            win = true;
            alert("Parabens Usuario 1 ganhou ")
            setBorderWinner (resOne,resTwo,resThree,resFour,resFive,resSix,resSeven,resEight,resNine)
            setTimeout(function() { window.location.reload(true);},800)
        }
    }
    else{
        checkBoxUserTwo.push(btn)
        resOne = checkBoxUserTwo.indexOf("btnOne") // variavel responsavel por verificar se o usuario 2 já apertou na minha div 01
        resTwo = checkBoxUserTwo.indexOf("btnTwo") // variavel responsavel por verificar se o usuario 2 já apertou na minha div 02
        resThree = checkBoxUserTwo.indexOf("btnThree") // variavel responsavel por verificar se o usuario 2 já apertou na minha div 03
        resFour = checkBoxUserTwo.indexOf("btnFour") // variavel responsavel por verificar se o usuario 2 já apertou na minha div 04
        resFive = checkBoxUserTwo.indexOf("btnFive") // variavel responsavel por verificar se o usuario 2 já apertou na minha div 05
        resSix = checkBoxUserTwo.indexOf("btnSix") // variavel responsavel por verificar se o usuario 2 já apertou na minha div 06
        resSeven = checkBoxUserTwo.indexOf("btnSeven") // variavel responsavel por verificar se o usuario 2 já apertou na minha div 07
        resEight = checkBoxUserTwo.indexOf("btnEight") // variavel responsavel por verificar se o usuario 2 já apertou na minha div 08
        resNine = checkBoxUserTwo.indexOf("btnNine") // variavel responsavel por verificar se o usuario 2 já apertou na minha div 09
        if (
            resOne != -1 && resFive != -1 && resNine != -1
            || resThree != -1 && resFive!= -1 && resSeven != -1

             || resOne != -1 && resFour != -1 && resSeven != -1 
             || resTwo != -1 && resFive != -1 && resEight != -1
             || resThree != -1 && resSix != -1 && resNine != -1 

             || resOne != -1 && resTwo != -1 && resThree != -1 
             || resFour!= -1 && resFive != -1 && resSix!= -1 
             || resSeven!= -1 && resEight!= -1 && resNine != -1 
            ) {
            win = true;
            alert("Parabens Usuario 2 ganhou ")
            setBorderWinner (resOne,resTwo,resThree,resFour,resFive,resSix,resSeven,resEight,resNine)
            setTimeout(function() { window.location.reload(true);},800)
        }

    }


}

function setBorderWinner (resOne,resTwo,resThree,resFour,resFive,resSix,resSeven,resEight,resNine) {

    if (
        resOne != -1 && resFive != -1 && resNine != -1
    ) {
        document.getElementById('boxOne').classList.add('winner');
        document.getElementById('boxFive').classList.add('winner');
        document.getElementById('boxNine').classList.add('winner');
    } else if (
        resThree != -1 && resFive != -1 && resSeven != -1
    ) {
        document.getElementById('boxThree').classList.add('winner');
        document.getElementById('boxFive').classList.add('winner');
        document.getElementById('boxSeven').classList.add('winner');
    } else if (
        // Adicione mais possibilidades aqui
        resOne != -1 && resTwo != -1 && resThree != -1
    ) {
        document.getElementById('boxOne').classList.add('winner');
        document.getElementById('boxTwo').classList.add('winner');
        document.getElementById('boxThree').classList.add('winner');
    } else if (
        resFour != -1 && resFive != -1 && resSix != -1
    ) {
        document.getElementById('boxFour').classList.add('winner');
        document.getElementById('boxFive').classList.add('winner');
        document.getElementById('boxSix').classList.add('winner');
    } else if (
        resSeven != -1 && resEight != -1 && resNine != -1
    ) {
        document.getElementById('boxSeven').classList.add('winner');
        document.getElementById('boxEight').classList.add('winner');
        document.getElementById('boxNine').classList.add('winner');
    } else if (
        resOne != -1 && resFour != -1 && resSeven != -1
    ) {
        document.getElementById('boxOne').classList.add('winner');
        document.getElementById('boxFour').classList.add('winner');
        document.getElementById('boxSeven').classList.add('winner');
    } else if (
        resTwo != -1 && resFive != -1 && resEight != -1
    ) {
        document.getElementById('boxTwo').classList.add('winner');
        document.getElementById('boxFive').classList.add('winner');
        document.getElementById('boxEight').classList.add('winner');
    } else if (
        resThree != -1 && resSix != -1 && resNine != -1
    ) {
        document.getElementById('boxThree').classList.add('winner');
        document.getElementById('boxSix').classList.add('winner');
        document.getElementById('boxNine').classList.add('winner');
    }
    



}

boxOne.addEventListener("click", ()=>{
    if (boxOneClick){
        alert("Essa opção já foi selecionada")

    }else{
        userClick (boxOne,"btnOne")
        boxOneClick = true
        CheckTied()
    }
       
})
boxTwo.addEventListener("click", ()=>{
    if (boxTwoClick){
        alert("Essa opção já foi selecionada")

    }else{
        userClick (boxTwo,"btnTwo")
        boxTwoClick = true
        CheckTied()
    }
})
boxThree.addEventListener("click", ()=>{
    if (boxThreeClick){
        alert("Essa opção já foi selecionada")

    }else{
        userClick (boxThree,"btnThree")
        boxThreeClick = true
        CheckTied()
    }
})
boxFour.addEventListener("click", ()=>{
    if (boxFourClick){
        alert("Essa opção já foi selecionada")

    }else{
        userClick (boxFour,"btnFour")
        boxFourClick = true
        CheckTied()
    }
})
boxFive.addEventListener("click", ()=>{
    if (boxFiveClick){
        alert("Essa opção já foi selecionada")

    }else{
        userClick (boxFive,"btnFive")
        boxFiveClick = true
        CheckTied()
    }
})
boxSix.addEventListener("click", ()=>{
    if (boxSixClick){
        alert("Essa opção já foi selecionada")

    }else{
        userClick (boxSix,"btnSix")
        boxSixClick = true
        CheckTied()
    }
})
boxSeven.addEventListener("click", ()=>{
    if (boxSevenClick){
        alert("Essa opção já foi selecionada")

    }else{
        userClick (boxSeven,"btnSeven")
        boxSevenClick = true
        CheckTied()
    }
})
boxEight.addEventListener("click", ()=>{
    if (boxEightClick){
        alert("Essa opção já foi selecionada")

    }else{
        userClick (boxEight,"btnEight")
        boxEightClick = true
        CheckTied()
    }
})
boxNine.addEventListener("click", ()=>{
    if (boxNineClick){
        alert("Essa opção já foi selecionada")

    }else{
        userClick (boxNine,"btnNine")
        boxNineClick = true
        CheckTied()
    }
})