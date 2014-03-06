$( document ).ready(function() {
   
	$("#login").on("click", mostrarFormulario);
});

function mostrarFormulario()
{
	$("#content-login").slideToggle();
	return false;
}
