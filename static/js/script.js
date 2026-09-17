function cadastrar(event) {
    event.preventDefault();

    alert("Evento cadastrado com sucesso!");

    event.target.reset();
}

function editar(event) {
    event.preventDefault();

    alert("Evento atualizado com sucesso!");
}

function excluir() {
    const confirmar = confirm(
        "Deseja realmente excluir este evento?"
    );

    if (confirmar) {
        let form = document.getElementsByClassName("form-del")[0];
        form.submit();
        alert("Evento excluído com sucesso!");
    }
}
