document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll(".jogos, h1, form, .detalhe-container");
    elements.forEach(el => setTimeout(() => el.classList.add("show"), 80));
});

const buscaJogo = document.getElementById('busca-jogo');
const filtroGenero = document.getElementById('filtro-genero');
const jogos = document.querySelectorAll('.jogos');

function filtrarJogos() {
    const busca = buscaJogo.value.toLowerCase();
    const genero = filtroGenero.value.toLowerCase();

    jogos.forEach(jogo => {
        const nome = jogo.querySelector('h3').innerText.toLowerCase();
        const generoJogo = jogo.querySelector('p').innerText.toLowerCase();

        if (nome.includes(busca) && (genero === "" || generoJogo.includes(genero))) {
            jogo.style.display = '';
        } else {
            jogo.style.display = 'none';
        }
    });
}

buscaJogo.addEventListener('input', filtrarJogos);
filtroGenero.addEventListener('change', filtrarJogos);
