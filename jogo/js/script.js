var  valores;
function verificarResposta(){
    var resposta = document.getElementById('resposta').value;
    var resposta_certa = valores.resposta;
    var resposta_alerta = document.getElementById('resposta-alerta');

    if(resposta == resposta_certa){
        resposta_alerta.innerText = "Resposta correta! Parabéns!";            
        resposta_alerta.classList.add('alert-success');
        
    }else{
        resposta_alerta.innerText = "Resposta errada. A resposta certa é: " +resposta_certa;
        resposta_alerta.classList.add('alert-danger');
    }
}

function iniciarJogo(){
    $.ajax({
        url: "jogar",
        type: "get",
        datatype: "json",
        success: function(data){
                valores = data.resposta;
                document.getElementById('numero_1').value = valores.numero1;
                document.getElementById('numero_2').value = valores.numero2;
                document.getElementById('operacao').value = valores.operacao;
                
        }
    });
}