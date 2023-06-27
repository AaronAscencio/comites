$(function () {

    var buttonCommon = {
        exportOptions: {
            format: {
                body: function ( data, row, column, node ) {
                    
                    if(column === 6){
                        let content_hipervinculo = data;
                        let substring = content_hipervinculo.slice(content_hipervinculo.indexOf('"')+1);
                        substring = substring.slice(0,substring.indexOf('"'));
                        if(substring.charAt(0) === '/') {
                            return window.location.host + substring;
                        }
                        //return window.location.host + substring;
                        return substring;
                    }

                    if(column == 7){
                        return '';
                    }
                    return data;

                }
            }
        }
    };


    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            }, // parametros
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "numero"},
            {"data": "referente.nombre"},
            {"data": "referente.apellido_paterno"},
            {"data": "referente.apellido_materno"},
            {"data": "referente.tipo_referente"},
            {"data": "id"}
        ],
        columnDefs: [

            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    let buttons = '<a href="/folio/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit fa-2x"></i></a> ';
                    buttons += '<a href="/folio/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt fa-2x"></i></a>';
                    return buttons;
                }
            }
        ],
        dom: 'Bfrtip',
        buttons: [
            $.extend( true, {}, buttonCommon, {
                extend: 'excelHtml5',
                text: 'Descargar Excel <i class="fas fa-file-excel"> </i>',
                titleAttr: 'Excel',
                className: 'btn btn-success btn-flat btn-xs'
                
            } ),
        ],
        initComplete: function(settings, json) {
        
          }
        });


});