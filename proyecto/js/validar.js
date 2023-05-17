//funcion que valida un formulario
$(function(){
    $("#mi-formulario").validate({
        rules: {
            nom: {
                required:true
            },
            correo: {
                required:true,
                email: true
            },
            pass: {
                required:true
            },
            fono:{
                required:true,
                number:true
            },
            fecha:{
                required:true
            },
            pass2: {
                required:true,
                equalTo:pass
            }
        },//rules
        messages:{
            nom:{
                required:'Ingrese nombre de usuario',
                minlength:'Formato incorrecto de nombre (3)'
            },
            correo:{
                required:'Ingrese correo de usuario',
                email:'Formato de correo inválido'
            },
            pass:{
                required:'Ingrese contraseña',
                minlength:'La cantidad de caracteres es insuficiente(8)'
            },
            fono:{
                required:'Ingrese número de teléfono',
                minlength:'Cantidad de digitos insuficientes(9)'
            },
            fecha:{
                required:'Seleccione una fecha válida',
                min:'Su fecha no cumple el valor minimo solicitado'
            },
            pass2:{
                required:'Confirme contraseña',
                minlength:'La cantidad de caracteres es insuficiente',
                equalTo:'La contraseña no coincide'
            },
        },//messages
    })
});