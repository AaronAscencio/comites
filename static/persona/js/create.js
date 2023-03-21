$(function(){

    $('.select2').select2({
        theme:'bootstrap',
        language:'es'
    });

    // Distritos 
    var select_distritos = $('select[name="distrito"]');
    // Municipios
    var select_municipios = $('select[name="municipio"]');
    var municipios_options = '<option value="">--------------------</option>';
    select_municipios.html(municipios_options);
    // Secciones
    var select_secciones = $('select[name="seccion"]');
    var secciones_options = '<option value="">--------------------</option>';
    select_secciones.html(secciones_options);

    $('select[name="distrito"]').on('change',function(){
        var id = $(this).val();
        var select_municipios = $('select[name="municipio"]');
        var municipios_options = '<option value="">--------------------</option>';
                if (id === '') {
                    select_municipios.html(municipios_options);
                    return false;
                }
                $.ajax({
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_municipios',
                        'id': id
                    },
                    dataType: 'json',
                }).done(function (data) {
                    //console.log(data)
                    if (!data.hasOwnProperty('error')) {
                        select_municipios.html('').select2({
                            theme: "bootstrap4",
                            language: 'es',
                            data: data
                        });
                        $.each(data, function (key, value) {
                            municipios_options += '<option value="' + value.id + '">' + value.text + '</option>';
                        });
                        return false;
                    }
                    message_error(data.error);
                }).fail(function (jqXHR, textStatus, errorThrown) {
                    alert(textStatus + ': ' + errorThrown);
                }).always(function (data) {
                    select_municipios.html(municipios_options);
                });
    });

    $('select[name="municipio"]').on('change',function(){
        var id = $(this).val();
        var select_secciones = $('select[name="seccion"]');
        var secciones_options = '<option value="">--------------------</option>';
                if (id === '') {
                    select_secciones.html(secciones_options);
                    return false;
                }
                $.ajax({
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_secciones',
                        'id': id
                    },
                    dataType: 'json',
                }).done(function (data) {
                    //console.log(data)
                    if (!data.hasOwnProperty('error')) {
                        select_secciones.html('').select2({
                            theme: "bootstrap4",
                            language: 'es',
                            data: data
                        });
                        $.each(data, function (key, value) {
                            secciones_options += '<option value="' + value.id + '">' + value.text + '</option>';
                        });
                        return false;
                    }
                    message_error(data.error);
                }).fail(function (jqXHR, textStatus, errorThrown) {
                    alert(textStatus + ': ' + errorThrown);
                }).always(function (data) {
                    select_secciones.html(secciones_options);
                });
    });

    let action = $("input[name='action']").val();
    if(action === 'edit'){
        var municipio_options = '<option value="">--------------------</option>';
        var seccion_options = '<option value="">--------------------</option>';
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'set_selects',
            },
            dataType: 'json',
        }).done(function (data) {
            console.log(data);
            
            if (!data.hasOwnProperty('error')) {
                console.log(data);
                select_municipios.html('').select2({
                    theme: "bootstrap4",
                    language: 'es',
                    data: data
                });
                $.each(data['municipios'], function (key, value) {
                    municipio_options += '<option value="' + value.id + '">' + value.text + '</option>';
                });
                $.each(data['secciones'], function (key, value) {
                    seccion_options += '<option value="' + value.id + '">' + value.text + '</option>';
                });
                return false;
            }
            message_error(data.error);
            
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert(textStatus + ': ' + errorThrown);
        }).always(function (data) {
            select_municipios.html(municipio_options);
            select_secciones.html(seccion_options);
            select_distritos.val(`${data['distrito_selected']}`).trigger("change.select2");
            select_municipios.val(`${data['municipio_selected']}`).trigger("change.select2");
            select_secciones.val(`${data['seccion_selected']}`).trigger("change.select2");
        });
    }
});