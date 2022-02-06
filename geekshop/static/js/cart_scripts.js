window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function (event) {
        var t_href = event.target;

        $.ajax({
            url: "/cart/edit/" + t_href.name + "/" + t_href.value + "/",

            success: function (data) {
                $('.basket_list').text = data.result;
            },
        });

        event.preventDefault();
    });
}
