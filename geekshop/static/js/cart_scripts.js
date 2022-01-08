window.onload = function () {
    document.querySelector('.basket_list input[type="number"]').addEventListener('click', function (event) {
        const href = event.target;

        fetch(`/cart/edit/${href.name}/${href.value}/`)
            .then((data) => data.json())
            .then((json) => {
                document.querySelectorAll("basket_list").innerHTML = json.result;
            })
        event.preventDefault();
    })
}
