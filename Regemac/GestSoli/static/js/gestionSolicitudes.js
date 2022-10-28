(function(){
    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn=> {
        btn.addEventListener('click',(e) =>{
            const confirmacion = confirm('¿Desea eliminar la solicitud??');
            if(!confirmacion) {
                e.preventDefault();
            }
        });
    });
})();