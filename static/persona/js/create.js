$(function(){

    $('.select2').select2({
        theme:'bootstrap',
        language:'es'
    });

    $('#id_codigo_postal').prop('readonly', true);

    // Distritos 
    var select_distritos = $('select[name="distrito"]');
    // Colonias 
    var select_colonias = $('select[name="colonia"]');
    var colonias_options = '<option value="">--------------------</option>';
    select_colonias.html(colonias_options);
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

        var select_secciones = $('select[name="seccion"]');
        var secciones_options = '<option value="">--------------------</option>';

        var select_colonias = $('select[name="colonia"]');
        var colonias_options = '<option value="">--------------------</option>';
                if (id === '') {
                    select_municipios.html(municipios_options);
                    select_secciones.html(secciones_options);
                    select_colonias.html(colonias_options);
                    $('#id_codigo_postal').val('');
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
                    select_secciones.html(secciones_options);
                    select_colonias.html(colonias_options);
                    $('#id_codigo_postal').val('');
                });
    });

    $('select[name="municipio"]').on('change',function(){
        var id = $(this).val();
        var select_secciones = $('select[name="seccion"]');
        var secciones_options = '<option value="">--------------------</option>';

        var select_colonias = $('select[name="colonia"]');
        var colonias_options = '<option value="">--------------------</option>';
                if (id === '') {
                    select_secciones.html(secciones_options);
                    select_colonias.html(colonias_options);
                    $('#id_codigo_postal').val('');
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
                    select_colonias.html(colonias_options);
                    $('#id_codigo_postal').val('');
                });
    });

    $('select[name="seccion"]').on('change',function(){
        var id = $(this).val();
        var select_colonias = $('select[name="colonia"]');
        var colonias_options = '<option value="">--------------------</option>';
        if (id === '') {
            select_colonias.html(colonias_options);
            $('#id_codigo_postal').val('');
            return false;
        }
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search_colonias',
                'id': id
            },
            dataType: 'json',
        }).done(function (data) {
            //console.log(data)
            if (!data.hasOwnProperty('error')) {
                select_colonias.html('').select2({
                    theme: "bootstrap4",
                    language: 'es',
                    data: data
                });
                $.each(data, function (key, value) {
                    colonias_options += '<option value="' + value.id + '">' + value.text + '</option>';
                });
                return false;
            }
            message_error(data.error);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert(textStatus + ': ' + errorThrown);
        }).always(function (data) {
            select_colonias.html(colonias_options);
            $('#id_codigo_postal').val('');
        });

    });

    $('select[name="colonia"]').on('change',function(){
        var id = $(this).val();
        //var select_colonias = $('select[name="colonia"]');
        //var colonias_options = '<option value="">--------------------</option>';
        if (id === '') {
            //select_colonias.html(colonias_options);
            return false;
        }
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search_cp',
                'id': id
            },
            dataType: 'json',
        }).done(function (data) {
            //console.log(data)
            if (!data.hasOwnProperty('error')) {
                codigo_postal = data.cp;
                $('#id_codigo_postal').val(codigo_postal);
                /*
                select_colonias.html('').select2({
                    theme: "bootstrap4",
                    language: 'es',
                    data: data
                });
                $.each(data, function (key, value) {
                    colonias_options += '<option value="' + value.id + '">' + value.text + '</option>';
                });*/

                return false;
            }
            message_error(data.error);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert(textStatus + ': ' + errorThrown);
        }).always(function (data) {
            //select_colonias.html(colonias_options);
        });
    });


    let action = $("input[name='action']").val();
    if(action === 'edit'){
        var municipio_options = '<option value="">--------------------</option>';
        var seccion_options = '<option value="">--------------------</option>';
        var colonia_options = '<option value="">--------------------</option>';
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'set_selects',
            },
            dataType: 'json',
        }).done(function (data) {
            
            if (!data.hasOwnProperty('error')) {
                
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
                $.each(data['colonias'], function (key, value) {
                    colonia_options += '<option value="' + value.id + '">' + value.text + '</option>';
                });
                return false;
            }
            message_error(data.error);
            
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert(textStatus + ': ' + errorThrown);
        }).always(function (data) {
            select_municipios.html(municipio_options);
            select_secciones.html(seccion_options);
            select_colonias.html(colonia_options)
            select_distritos.val(`${data['distrito_selected']}`).trigger("change.select2");
            select_municipios.val(`${data['municipio_selected']}`).trigger("change.select2");
            select_secciones.val(`${data['seccion_selected']}`).trigger("change.select2");
            select_colonias.val(`${data['colonia_selected']}`).trigger("change.select2");
        });
    }
});