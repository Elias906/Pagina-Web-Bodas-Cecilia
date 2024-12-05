$(document).ready(function () {
  var formularioEnviado = false; // Bandera para verificar si el formulario ya ha sido enviado

  $('form').submit(function (event) {
    event.preventDefault(); // Evita que se realice la acción predeterminada del formulario

    if (formularioEnviado) {
      return; // Si el formulario ya ha sido enviado, no realizar ninguna acción adicional
    }

    formularioEnviado = true; // Establecer la bandera del formulario como enviado
    $('body').addClass('loading'); // Agrega la clase "loading" al body
    var submitButton = $('input[type="submit"]');
    $('.container-xxl').addClass('loading'); // Agrega la clase "loading" al contenedor principal
    submitButton.prop('disabled', true); // Deshabilita el botón de envío
    submitButton.addClass('loading'); // Agrega la clase "loading" al botón

    // Realizar la petición AJAX
    $.ajax({
      url: '/contacto', // Obtén la URL del formulario
      type: 'POST', // Obtén el método del formulario (POST)
      data: $(this).serialize(), // Obtén los datos del formulario
      crossDomain: true,

      success: function (response) {
        $('body').removeClass('loading'); // Quita la clase "loading" del body
        $('.container-xxl').removeClass('loading'); // Quita la clase "loading" del contenedor principal
        submitButton.prop('disabled', false); // Habilita el botón de envío
        submitButton.removeClass('loading'); // Quita la clase "loading" del botón
        Swal.fire({
          title: '¡Mensaje enviado!',
          text: 'Gracias por contactarnos. Nos pondremos en contacto contigo pronto.',
          icon: 'success',
          confirmButtonText: 'Aceptar',
          confirmButtonColor: '#000000'
        }).then(function () {
          window.location.href = "/contacto"; // Redirigir al usuario a la página de inicio
        });
        $('form').off('submit'); // Desvincula el evento submit después del primer envío exitoso
      },

      error: function (error) {
        $('body').removeClass('loading'); // Quita la clase "loading" del body
        $('.container-xxl').removeClass('loading'); // Quita la clase "loading" del contenedor principal
        submitButton.prop('disabled', false); // Habilita el botón de envío
        submitButton.removeClass('loading'); // Quita la clase "loading" del botón
        Swal.fire({
          title: 'Error',
          text: 'Ocurrió un error al enviar el mensaje. Por favor, inténtalo de nuevo más tarde.',
          icon: 'error',
          confirmButtonText: 'Aceptar'
        }).then(function () {
          window.location.href = "/contacto"; // Redirigir al usuario a la página de inicio
        });
        $('form').off('submit'); // Desvincula el evento submit después del primer error de envío
      }
    });
  });
});

/* $(document).ready(function (){
  let celular = document.getElementById('celular');

  celular.addEventListener('keypress', function(event){
    if(celular.value == 'A'){
      
    }
  });
}); */

/* $(document).ready(function () {  

  let forma = document.getElementById('formulario');
  let nombres = document.getElementById('nombres');
  let apellidos = document.getElementById('apellidos');
  let celular = document.getElementById('celular');
  let correo = document.getElementById('correo');
  let mensaje = document.getElementById('mensaje');
  let envio = document.getElementById('enviarMensaje');
 

  envio.addEventListener('click', function(event){
    
    event.preventDefault();

    let mensajes_errores = document.getElementById('mensajes-error');
    mensajes_errores.innerHTML = '';

    let errores = [];

    if(nombres.value == ''){
      errores.push('El campo nombre no puede estar vacío.');
      nombres.style.borderBlockColor = 'red';
    }else{
      nombres.style.borderBlockColor = '';
    }

    if(errores != ''){

      for(let i = 0; i < errores.length; i++){
        mensajes_errores.innerHTML += errores[i];
      }

      console.log(errores);      
            
      mensajes_errores.className = 'mostrar';      

      console.log(mensajes_errores);

      forma.onsubmit = 'false';
    }else{
      forma.onsubmit = 'true';
    }
  });
}); */