

formulario.addEventListener("submit",
function (evento) {
evento.preventDefault(); // o navegador NAO envia
var dados = {
nome: document.getElementById("nome").value,
data: document.getElementById("data").value
};
fetch("/api/eventos", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify(dados)
})
})

function acrescentarNaLista(dados) {
var item = document.createElement("li");
// textContent, NUNCA innerHTML, para conteudo
item.textContent = dados.nome + " — " + dados.data;
lista.appendChild(item); // agora ele aparece
}
function desenharLista(eventos) {
lista.innerHTML = ""; // esvaziar e inofensivo
for (var i = 0; i < eventos.length; i = i + 1) {
acrescentarNaLista(eventos[i]);
}
}
