// $("#techno").submit(function (e){
//     e.preventDefault();
//     var serializedData = $(this).serialize();
//         console.log(serializedData)
//         $.ajax({
//             type: "POST",
//             url: "/companies/technologies/add/",
//             data: serializedData,
//             success: function (response) {
//                 $("#techno").trigger('reset');
//                 $("#techno-input").focus();
//                 var instance = JSON.parse(response['instance']);
//                 var fields = instance[0]['fields']
//                 $("#technologies tbody").append(
//                     `<tr>
//                         <td>${fields["name"]||""}</td>
//                     </tr>`
//                 )
//             },
//             error: function (response) {
//                 alert(response["responseJSON"]["error"]);
//             }
//         })
//     })
//
// $("#industry").submit(function (e){
//     e.preventDefault();
//     var serializedData = $(this).serialize();
//     console.log(serializedData)
//     $.ajax({
//         type: "POST",
//         url: "/companies/industries/add/",
//         data: serializedData,
//         success: function (response) {
//             $("#industry").trigger('reset');
//             $("#industry-input").focus();
//             var instance = JSON.parse(response['instance']);
//             var fields = instance[0]['fields']
//             $("#industries tbody").append(
//                 `<tr>
//                     <td>${fields["name"]||""}</td>
//                 </tr>`
//             )
//         },
//         error: function (response) {
//             alert(response["responseJSON"]["error"]);
//         }
//     })
// })


//
//
// $("#modal-technology").on("submit", ".js-technology-create-form", function () {
//     var form = $(this);
//     $.ajax({
//         url: form.attr("action"),
//         data: form.serialize(),
//         type: form.attr("method"),
//         dataType: 'json',
//         success: function (data) {
//             if (data.form_is_valid) {
//                 var mess =  $("#technology-success")
//                 mess.show()
//                 mess.fadeOut(3000)
//                 $("#modal-technology").trigger('reset');
//                 $("#techno-input").focus();
//             }
//             else {
//                 $("#modal-technology .modal-content").html(data.html_form);
//             }
//         }
//     });
//     return false;
// });
//
    $(".js-create-technology").click( function () {
        var btn = $(this)
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-technology").modal("show");
            },
            success: function (data) {
                $("#modal-technology .modal-content").html(data.html_form)
            }
        });
    });
//
//
//
// $(function () {
//
//     var loadForm = function () {
//         var btn = $(this);
//         console.log(btn.attr("data-url"))
//         $.ajax({
//             url: btn.attr("data-url"),
//             type: "get",
//             dataType: 'json',
//             beforeSend: function () {
//                 $("#modal-technology").modal("show");
//             },
//             success: function (data) {
//                 $("#modal-technology .modal-content").html(data.html_form);
//             }
//         });
//     };
//
//
//     var saveForm = function () {
//         var form = $(this);
//         $.ajax({
//             url: form.attr("action"),
//             data: form.serialize(),
//             type: form.attr("method"),
//             dataType: 'json',
//             success: function (data) {
//                 if (data.form_is_valid) {
//                     $("#technology-table tbody").html(data.html_technology_list);
//                     $("#modal-technology").modal("hide");
//                 }
//                 else {
//                     $("#modal-technology .modal-content").html(data.html_form);
//                 }
//             }
//         });
//         return false;
//     };
//
//     $(".js-create-technology").click(loadForm);
//     $("#modal-technology").on("submit", ".js-technology-create-form", saveForm);
//
// });






function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

$('.js-technology-delete').on("click",  function () {
    var data = $(this);
    $.ajax({
        url: data.attr("data-url"),
        type: 'post',
        headers: {'X-CSRFToken': csrftoken},
        beforeSend: function () {
        },
        success: function () {
            var mess =  $("#technology-deleted")
            mess.show()
            mess.fadeOut(3000)
            data.parents('tr').remove()
        }
    })
});
