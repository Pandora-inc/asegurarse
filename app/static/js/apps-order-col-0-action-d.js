$(document).ready(function () {
    $('#listado').dataTable( {
        columnDefs: [
            { orderable: false, targets: 1 }
        ],
        order: [[0, 'desc']],
        "language": {
        "search": "Filtro:",
        "paginate": {
            "previous": "Anterior",
            "next": "Siguiente"
        },
        "lengthMenu": "Mostrar _MENU_ registros",
        "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
        "infoEmpty": "Mostrando 0 a 0 de 0 registros",
        "infoFiltered": "(filtrados de _MAX_ registros en total)",
      }
    } );
});